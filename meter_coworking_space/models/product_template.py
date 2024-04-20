# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.template'

    space_ok = fields.Boolean(
        string="Is Coworking Space",
        help="Coworking space product.")

    floor_id = fields.Many2one(comodel_name='mtr_coworking.floor', string='Floor')

    @api.onchange('space_ok')
    def _onchange_is_coworking_space(self):
        for space in self:
            if space.space_ok == True:
                category = self.env.ref('meter_coworking_space.coworking_category')
                space.public_categ_ids = [(6, 0, [category.id])]