## Context

`agreement` (OCA 18.0) har redan det ett PUB behöver:

```
agreement.code, name, partner_id, agreement_type_id,
signature_date, start_date, end_date, is_template, domain
```

`agreement.type` har `name` och `domain` (`sale`/`purchase`). GDPR-typerna
(PUB, SCC, Art. 26) passar inte i den indelningen — de är inte sälj- eller
inköpsavtal, de är *regelefterlevnadsinstrument*.

`gdpr_inventory` (repo `odoo-gdpr`) är klar: 61/92 tasks, installerar,
Art. 30-fälten finns.

## Goals / Non-Goals

**Goals:**
- Koppla avtal till inventering utan att duplicera avtalsregistret.
- Tillhandahålla GDPR-avtalstyperna.
- Varna vid saknat avtal, blockera vid utgånget.

**Non-Goals:**
- Ingen egen avtalsmodell.
- Ingen avtalsgenerering (mall → PDF). Det är `sign_gdpr`/`dms_gdpr`.
- Ingen signering. Det är `sign_gdpr` i `odoo-sign`.
- Ingen dokumentförvaring. Det är `dms_gdpr` i `odoo-document`.

## Decisions

### D1. Saknat avtal varnar, utgånget blockerar

**Varför:** Ett saknat avtal är ofta ett pågående arbete — avtalet är hos
motparten för underskrift. Att blockera då stoppar verksamheten utan att lösa
något. Ett **utgånget** avtal är däremot ett faktum: behandlingen sker utan
giltig grund, och då ska den stoppas.

**Alternativ:** blockera båda. Förkastat — samma skäl som `dry_run` i
`gdpr_inventory`: ett system som stoppar arbete kringgås.

### D2. `agreement_type_id` med `domain='purchase'`, inte en ny selection

**Varför:** `agreement.domain` är `sale`/`purchase`. Ett PUB vi tecknar med en
leverantör är ett inköpsavtal i den modellens mening. Att lägga till en tredje
domän (`gdpr`) hade krävt en ändring i `agreement`-modulen, vilket bryggan inte
får göra.

**Hur:** de fyra GDPR-typerna skapas som `agreement.type`-poster med
`domain='purchase'`. Deras `name` säger vad de är.

⚠ **Fälla:** om kunden redan har en `agreement.type` som heter "Data Processing
Agreement" skapas en dubblett. Skapa med fasta xmlid och `noupdate="1"` så att
en uppgradering inte skriver över kundens egna.

### D3. Varningen bor på inventeringen, inte på avtalet

**Varför:** Det är inventeringen som är behandlingen. Avtalet vet inte vilka
inventeringar det täcker — det är kopplingen som vet.

**Hur:** `gdpr.inventory` får en compute `_compute_agreement_warning()` som
läser `agreement_ids` och sätter `agreement_warning` (Html) + `agreement_state`
(`ok`/`missing`/`expiring`/`expired`).

### D4. Aktiveringsspärren ligger i `action_activate`, inte i en constraint

**Varför:** En `@api.constrains` på `state` fyrar även vid dataimport och vid
`write()` från andra moduler. Vi vill bara spärra den **avsiktliga**
aktiveringen.

⚠ **Fälla:** `gdpr.inventory` har ingen `action_activate` idag — `state` är en
vanlig selection. Bryggan måste antingen lägga till en, eller spärra i
`write()`. **Open question 1.**

## Risks / Trade-offs

| Risk | Mitigering |
|---|---|
| **Dubblett av avtalstyp** | Fasta xmlid + `noupdate="1"` |
| **Spärren fyrar vid import** | Spärr i action, inte constraint (D4) |
| **Två avtalsregister glider isär** | Bryggan äger ingen avtalsmodell |
| **`agreement` saknas i kundens installation** | Bryggan är inte `auto_install`; den installeras bara där `agreement` finns |

## Migration Plan

1. Skapa `agreement_gdpr` med beroenden
2. `data/*.xml`: fyra `agreement.type`-poster
3. Many2many `gdpr.inventory.agreement_ids` + invers på `agreement`
4. Compute: `agreement_state` + `agreement_warning`
5. Aktiveringsspärr (se open question 1)
6. Test: PUB kopplad → ingen varning; utgången → blockerad

**Rollback:** avinstallation tar bort kopplingstabellen. Avtalen ligger kvar i
`agreement` — det är avsiktligt.

## Open Questions

1. **Var ska aktiveringsspärren sitta?** `gdpr.inventory` har ingen
   `action_activate` — `state` sätts direkt. Antingen lägger bryggan till en
   action (och då måste UI:t byta från statusbar till knapp), eller så spärras i
   `write()`. Det förra är renare men rör inventeringens UI.
2. **Vilka varningsfönster?** 30 dagar innan utgång? 90?
3. **Ska `agreement` få en `gdpr_inventory_ids`-invers, eller bara Many2many
   från inventeringen?** Inversen gör avtalet sökbart från GDPR-hållet.
