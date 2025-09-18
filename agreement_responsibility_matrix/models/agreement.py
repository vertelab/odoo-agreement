from odoo import models, fields, api


class Agreement(models.Model):
    _inherit = "agreement"

    agreement_responsibility_line_ids = fields.One2many(
        "agreement.responsibility.line", "agreement_id", "Agreement Responsibility Lines"
    )
    category_id = fields.Many2one('agreement.category', string='Category')
    parent_id = fields.Many2one('agreement', string='Parent Agreement', ondelete='cascade')
    child_ids = fields.One2many('agreement', 'parent_id', string='Child Agreements')

    
class AgreementCategory(models.Model):
    _name = 'agreement.category'
    _description = 'Agreement Category'
    _parent_name = 'parent_id'
    _parent_store = True

    name = fields.Char(required=True)
    parent_id = fields.Many2one('agreement.category', string='Parent Category', index=True, ondelete='cascade')
    child_ids = fields.One2many('agreement.category', 'parent_id', string='Children')
    
    parent_path = fields.Char(index=True)
