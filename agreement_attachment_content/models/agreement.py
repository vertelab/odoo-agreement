from odoo import models, fields, api


class Agreement(models.Model):
    _inherit = 'agreement'

    index_content = fields.Text(
        string='Index Content', compute='_compute_index_content', search='_search_index_content')

    def _compute_index_content(self):
        for agreement in self:
            attachments = self.env['ir.attachment'].search([
                ('res_id', '=', agreement.id),
                ('res_model', '=', 'agreement'),
                ('index_content', '!=', False),
            ])
            index_contents = attachments.mapped('index_content')
            agreement.index_content = '\n\n'.join(index_contents) if index_contents else ''

    def _search_index_content(self, operator, value):
        attachments = self.env['ir.attachment'].search([
            ('res_model', '=', 'agreement'),
            ('index_content', operator, value),
        ])
        agreement_ids = attachments.mapped('res_id')
        return [('id', 'in', agreement_ids)]
