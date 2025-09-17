from odoo import models, fields, api, _


class AgreementResponsibilityCategory(models.Model):
    _name = "agreement.responsibility.category"
    _description = "Agreement Responsibility Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name desc'

    name = fields.Char(string="Name", index='trigram', required=True)
    parent_id = fields.Many2one("agreement.responsibility.category", string="Parent", index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('agreement.responsibility.category', 'parent_id', 'Child Categories')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    agreement_responsibility_line_ids = fields.One2many(
        "agreement.responsibility.line", "agreement_responsibility_category_id", "Agreement Responsibility Lines"
    )