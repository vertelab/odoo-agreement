# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_categories',
    'name': 'Agreement: Categories',
    'summary': "Adds hierarchical categories to agreements.",
    'version': '18.0.1.2.0',
    'category': 'Agreement',
    'depends': ['agreement_legal', 'mail'],
    'description': '''
Categories
==========

    Adds hierarchical categories to agreements.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on agreement, agreement.category, complete_name, mail.thread.
    ''',
    'data': [
        'security/ir.model.access.csv',
        'views/agreement_category_views.xml',
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
