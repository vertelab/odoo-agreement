from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AgreementCategory(models.Model):
    _name = "agreement.category"
    _inherit = ['mail.thread']
    _description = "Agreement Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char('Name', index='trigram', required=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    parent_id = fields.Many2one('agreement.category', 'Parent Category', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('agreement.category', 'parent_id', 'Child Categories')
    agreement_count = fields.Integer(
        '# Agreement', compute='_compute_agreement_count',
        help="The number of agreements under this category (Does not consider the children categories)")
    agreement_properties_definition = fields.PropertiesDefinition('Agreement Properties')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_agreement_count(self):
        read_group_res = self.env['agreement']._read_group([
            ('category_id', 'child_of', self.ids)
        ], ['category_id'], ['__count'])
        group_data = {agreement_category.id: count for agreement_category, count in read_group_res}
        for agreement_category in self:
            agreement_count = 0
            for sub_agreement_category_id in agreement_category.search([('id', 'child_of', agreement_category.ids)]).ids:
                agreement_count += group_data.get(sub_agreement_category_id, 0)
            agreement_category.agreement_count = agreement_count

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if self._has_cycle():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        category = self.create({'name': name})
        return category.id, category.display_name

    @api.depends_context('hierarchical_naming')
    def _compute_display_name(self):
        if self.env.context.get('hierarchical_naming', True):
            return super()._compute_display_name()
        for record in self:
            record.display_name = record.name

    def action_view_agreements(self):
        pass