from odoo import models, fields, api, _


class AgreementResponsibilityLine(models.Model):
    _name = "agreement.responsibility.line"
    _description = "Agreement Responsibility Line"

    name = fields.Char(string="Name", index='trigram', required=True)
    owner = fields.Selection([('landlord', 'Landlord'), ('tenant', 'Tenant')], string="Owner", default="landlord")
    maintenance_responsibility = fields.Selection([
        ('landlord', 'Landlord'), ('tenant', 'Tenant')], string="Maintenance Responsibility", default="landlord")
    remarks = fields.Text(string="Remarks")
    agreement_responsibility_category_id = fields.Many2one("agreement.responsibility.category", string="Category")
    agreement_id = fields.Many2one("agreement", string="Agreement")
