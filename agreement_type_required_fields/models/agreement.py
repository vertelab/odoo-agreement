from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Agreement(models.Model):
    _inherit = "agreement"

    def _get_agreement_type_required_fields(self):
        if not self.agreement_type_id:
            return []
        return self.agreement_type_id.required_fields.filtered(lambda r: r.is_required)

    @api.constrains('agreement_type_id')
    def _check_required_fields(self):
        for record in self:
            if not record.agreement_type_id:
                continue

            required_fields = record._get_agreement_type_required_fields()
            missing_fields = []

            for req_field in required_fields:
                field_name = req_field.field_id.name

                if field_name not in record._fields: # Check if field exists in the model
                    continue

                field_value = record[field_name]

                if not field_value: # Check if field is empty
                    field_label = req_field.field_id.field_description or field_name
                    missing_fields.append(field_label)

            if missing_fields:
                raise ValidationError(
                    f"The following required fields are missing: {', '.join(missing_fields)}"
                )

    def write(self, vals):
        result = super().write(vals)
        if 'agreement_type_id' in vals or self.agreement_type_id:
            self._check_required_fields()
        return result