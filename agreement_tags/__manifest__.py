# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Agreement Tags',
    'version': '1.2',
    'category': 'Agreement',
    'depends': ['agreement_legal', 'mail'],
    'description': """This is module adds tags to agreement.""",
    'data': [
        'security/ir.model.access.csv',
        'views/agreement_tag_views.xml',
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
