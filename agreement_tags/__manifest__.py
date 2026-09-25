# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_tags',
    'name': 'Agreement: Tags',
    'summary': "Adds tags to agreements.",
    'version': '18.0.1.2.0',
    'category': 'Agreement',
    'depends': ['agreement_legal', 'mail'],
    'description': '''
Tags
====

    Adds tags to agreements.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on agreement, agreement.tag.
    ''',
    'data': [
        'security/ir.model.access.csv',
        'views/agreement_tag_views.xml',
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
