# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_attachment_content',
    'name': 'Agreement: Attachment Content',
    'version': '1.2',
    'category': 'Agreement',
    'depends': ['agreement_legal'],
    'description': """This is module agreegates contents of attachments.""",
    'data': [
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
