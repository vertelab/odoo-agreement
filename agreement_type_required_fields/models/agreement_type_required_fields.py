# Copyright (C) 2018 - TODAY, Pavlov Media
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AgreementTypeRequiredFields(models.Model):
    _name = "agreement.type.required.fields"
    _description = "Agreement Types Required Fields"

    field_id = fields.Many2one('ir.model.fields', string="Fields", domain=[("model_id.model", "=", 'agreement')])
    name = fields.Char(string="Name", related="field_id.name")
    is_required = fields.Boolean(string="Is Required")
    agreement_type_id = fields.Many2one('agreement.type', string="Agreement Type")


