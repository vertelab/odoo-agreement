from odoo import api, fields, models


class AgreementType(models.Model):
    _inherit = "agreement.type"

    required_fields = fields.One2many(
        "agreement.type.required.fields", "agreement_type_id", string="Required Fields", copy=False
    )