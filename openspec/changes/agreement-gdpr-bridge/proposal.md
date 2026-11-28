## Why

Article 28 requires a written contract between controller and processor. Article
26 requires one between joint controllers. Article 46 requires standard
contractual clauses for third-country transfers. The GDPR inventory records
*that* these arrangements exist — `role`, `data_sharing_ids`,
`third_country_ids`, `transfer_safeguards` — but not the agreements themselves.

`agreement` (OCA) already has `partner_id`, `agreement_type_id`,
`signature_date`, `start_date` and `end_date`. It is the right place for a
processing agreement. What is missing is the link to the inventory, and the
warning when the link is absent or expired.

Split out of `odoo-gdpr` change `gdpr-18-repair-and-extend` (group 9B). The
bridge belongs here because it touches `agreement` and `agreement.type` — and
because a GDPR module that owns an agreement register would be a second
agreement register that drifts from this one.

## What Changes

- New module `agreement_gdpr` with `agreement` and `gdpr_inventory` as
  dependencies.
- `gdpr.inventory.agreement_ids` — the agreements that govern a processing
  activity.
- Agreement types for the GDPR instrument set: data processing agreement
  (Art. 28), standard contractual clauses (Art. 46), joint controller
  arrangement (Art. 26), confidentiality undertaking.
- A warning on the inventory when it is a processor or shares data with a
  recipient but has no processing agreement linked.
- An expiry warning, and a block on activating an inventory whose processing
  agreement has lapsed.

## Capabilities

### New Capabilities
- `agreement-gdpr-bridge`: the `agreement_gdpr` module — linking agreements to
  inventories, the GDPR agreement types, and validity monitoring.

### Modified Capabilities
Inga.

## Impact

**Kod:** ny modul `agreement_gdpr` i `odoo-agreement`.

**Beroende:** `agreement` (OCA 18.0) och `gdpr_inventory` (change
`gdpr-18-repair-and-extend`).

**Juridik:** Art. 26 (gemensamt personuppgiftsansvar), Art. 28
(personuppgiftsbiträde), Art. 46 (tredjelandsöverföring).

**Risk:** medel. En blockerad aktivering är ett hårt ingrepp i ett arbetsflöde.
Den ska bara slå till när avtalet faktiskt löpt ut, inte när det saknas — ett
saknat avtal ska varna, inte stoppa.
