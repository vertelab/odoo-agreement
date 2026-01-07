from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Agreement(models.Model):
    _inherit = "agreement"

    is_confidential = fields.Boolean(string="Confidential", default=False, copy=False)