from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_space_order = fields.Boolean(
        string="Is Coworking Space Order",
        compute="_compute_is_space_order",
        store=True,
    )

    @api.depends("order_line.is_space")
    def _compute_is_space_order(self):
        for order in self:
            order.is_space_order = any(order.order_line.mapped("is_space"))

    def action_confirm(self):
        self.order_line._check_space_availability()
        return super().action_confirm()
