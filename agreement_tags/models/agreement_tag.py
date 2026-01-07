from random import randint

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AgreementTag(models.Model):
    _name = "agreement.tag"
    _description = "Agreement Tag"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)
    agreement_ids = fields.Many2many('agreement', 'agreement_tag_rel', 'tag_id', 'agreement_id', string='Agreements')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]
