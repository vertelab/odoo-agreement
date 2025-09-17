from odoo import models, fields, api


class Agreement(models.Model):
    _inherit = "agreement"

    agreement_responsibility_line_ids = fields.One2many(
        "agreement.responsibility.line", "agreement_id", "Agreement Responsibility Lines"
    )