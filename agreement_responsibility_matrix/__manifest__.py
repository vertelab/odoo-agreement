# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Agreement Responsibility Matrix",
    "summary": "Adds an agreement responsibility matrix",
    "version": "1.0.0",
    "category": "Contract",
    "author": "Vertel AB",
    "website": "https://github.com/vertelab/odoo-agreement",
    "license": "AGPL-3",
    "depends": ["agreement","agreement_legal"],

    "data": [
        "security/ir.model.access.csv",
        "views/agreement_view.xml",
        "views/agreement_responsibility_category_view.xml",
        'demo/agreement_demo.xml',
    ],
    'demo': [
        #'demo/agreement_demo.xml',
    ],
    "installable": True,
    'application': False,
}
