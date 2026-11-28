## 1. Modulstomme

- [ ] 1.1 Skapa `agreement_gdpr` med beroenden `agreement`, `gdpr_inventory`
- [ ] 1.2 Sätt `'auto_install': False`

## 2. Avtalstyper

- [ ] 2.1 Skapa `data/agreement_type_data.xml` med fyra `agreement.type`-poster:
      PUB (Art. 28), SCC (Art. 46), Joint controller (Art. 26), Confidentiality
- [ ] 2.2 Sätt `domain='purchase'` och `noupdate="1"`
- [ ] 2.3 Verifiera att en uppgradering inte skriver över kundens egna typer

## 3. Kopplingen

- [ ] 3.1 Lägg `agreement_ids` (Many2many) på `gdpr.inventory` via inherit
- [ ] 3.2 Lägg `gdpr_inventory_ids` (Many2many) på `agreement` via inherit
- [ ] 3.3 Verifiera att ett avtal kan täcka flera inventeringar utan dubblett

## 4. Varning

- [ ] 4.1 Compute `agreement_state` (`ok`/`missing`/`expiring`/`expired`)
- [ ] 4.2 Compute `agreement_warning` (Html) som namnger problemet
- [ ] 4.3 Visa varningen i inventeringens formvy
- [ ] 4.4 Varna när roll är `processor` utan PUB
- [ ] 4.5 Varna när mottagarkategorier finns utan PUB
- [ ] 4.6 Notifiera ansvarig vid `expiring`/`expired`

## 5. Aktiveringsspärr

- [ ] 5.1 Besvara open question 1 (action eller write)
- [ ] 5.2 Implementera spärren — bara vid `expired`, aldrig vid `missing`
- [ ] 5.3 Test: utgånget avtal blockerar aktivering
- [ ] 5.4 Test: saknat avtal blockerar inte

## 6. Avslut

- [ ] 6.1 Kör `openspec validate agreement-gdpr-bridge`
