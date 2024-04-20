# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.template'

    space_ok = fields.Boolean(
        string="Is Coworking Space",
        help="Coworking space product.")

    floor_id = fields.Many2one(comodel_name='mtr_coworking.floor', string='Floor')