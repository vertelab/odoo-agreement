from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class Agreement(models.Model):
    _inherit = "agreement"

    agreement_category_id = fields.Many2one('agreement.category', string="Category")
