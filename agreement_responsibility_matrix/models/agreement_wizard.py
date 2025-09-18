# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
import logging

class CreateAgreementWizard(models.TransientModel):
    _inherit = "create.agreement.wizard"
    
    def copy_matrix_from_template(self, agreement):
        for matrix_line in agreement.template_id.agreement_responsibility_line_ids:
            self.env['agreement.responsibility.line'].create({
            'name':matrix_line.name,
            'agreement_responsibility_category_id':matrix_line.agreement_responsibility_category_id.id,
            'remarks':matrix_line.remarks,
            'agreement_id':agreement.id,
            'owner':matrix_line.owner,
            'maintenance_responsibility':matrix_line.maintenance_responsibility,
             }
            )

    def _create_agreement(self):
        agreement = super(CreateAgreementWizard, self)._create_agreement()
        self.copy_matrix_from_template(agreement)
        return agreement
