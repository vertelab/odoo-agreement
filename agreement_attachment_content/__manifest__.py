# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'website': 'https://vertel.se/apps/odoo-agreement/agreement_attachment_content',
    'name': 'Agreement: Attachment Content',
    'summary': "Indexes the content of agreement attachments.",
    'version': '18.0.1.2.0',
    'category': 'Agreement',
    'depends': ['agreement_legal'],
    'description': '''
Attachment Content
==================

    Indexes the content of agreement attachments.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on agreement.
    ''',
    'data': [
        'views/agreement_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
