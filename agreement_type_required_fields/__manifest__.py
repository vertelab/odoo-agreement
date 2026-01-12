{
    'name': 'Agreement: Required Fields',
    'version': '1.0',
    'category': 'Agreement',
    'summary': 'Add required fields validation to agreement types',
    'description': """
        Agreement Required Fields
        =========================
        This module extends the agreement module to add:
        * Required fields configuration per agreement type
        * Automatic validation of required fields on create/write
    """,
    'author': 'Vertel AB',
    'website': 'https://www.vertel.se',
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
