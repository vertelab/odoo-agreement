# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_confidentiality',
    'name': 'Agreement: Confidentiality',
    'summary': "Marks agreements as confidential.",
    'version': '18.0.1.2.0',
    'category': 'Agreement',
    'depends': ['agreement_legal'],
    'description': '''
Confidentiality
===============

    Marks agreements as confidential.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on agreement.
    ''',
    'data': [
        'security/agreement_security.xml',
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
