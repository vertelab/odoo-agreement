{
    'name': 'Agreement: Required Fields',
    'version': '18.0.1.0.0',
    'category': 'Agreement',
    'summary': 'Add required fields validation to agreement types.',
    'description': '''
Required Fields
===============

    Agreement Required Fields
            =========================
            This module extends the agreement module to add:
            * Required fields configuration per agreement type
            * Automatic validation of required fields on create/write

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on agreement, agreement.type, agreement.type.required.fields.
    ''',
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_type_required_fields',
    'depends': [
        'agreement',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/agreement_type_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
