# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Agreement Confidentiality',
    'version': '1.2',
    'category': 'Agreement',
    'depends': ['agreement_legal'],
    'description': """This is module makes agreement confidential.""",
    'data': [
        'security/agreement_security.xml',
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
