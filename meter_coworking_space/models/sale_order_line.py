from pytz import timezone, UTC

from odoo import _, api, fields, models



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Stored because a product could have been rent_ok when added to the SO but then updated
    is_space = fields.Boolean(compute='_compute_is_space', store=True, precompute=True)
    is_product_space = fields.Boolean(related='product_id.space_ok', depends=['product_id'])
    @api.depends('product_id')
    def _compute_is_space(self):
        for line in self:
            line.is_space = line.is_product_space and line.env.context.get('in_meter_coworking_space_app')