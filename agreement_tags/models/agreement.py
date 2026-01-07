from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class Agreement(models.Model):
    _inherit = "agreement"

    tag_ids = fields.Many2many('agreement.tag', string="Tags")
