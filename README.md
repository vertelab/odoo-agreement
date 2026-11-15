# odoo-agreement — gren 19.0

> **Denna gren är avsiktligt tom.** Modulerna är INTE portade till Odoo 19.
> Grenen finns så att dev-miljöer (`hansolo19`) kan klona den utan att falla,
> men den påstår ingenting om att koden är portad.

## Baseline

| | |
|---|---|
| Källa | `20.0` |
| Moduler | **6** |
| Grenar i repot | `18.0`, `20.0`, `main` |

## Moduler

- `agreement_attachment_content`
- `agreement_categories`
- `agreement_confidentiality`
- `agreement_responsibility_matrix`
- `agreement_tags`
- `agreement_type_required_fields`

## Blockerare

**1 externa beroenden saknas** i Odoo 19-kärnan och OCA 19.0:

| Beroende | Behövs av |
|---|---|
| `agreement_legal` | `agreement_attachment_content`, `agreement_categories`, `agreement_confidentiality`, `agreement_responsibility_matrix` … |

### Prioritering

Ett beroende som blockerar många moduler ger mest nytta att lösa först:

- `agreement_legal` — frisläpper **5** modul(er)

## Nästa steg

Portering sker på `*-pfile`-maskin med versionsagnostisk kod
(`.p.py` / `.p.xml`). Se `/skill:odoo-pfiles`.
