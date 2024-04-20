# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta
from math import ceil

from odoo import _, api, fields, models
from odoo.osv import expression
from odoo.tools import float_compare



class SaleOrder(models.Model):
    _inherit = 'sale.order'


    #=== FIELDS ===#
    is_space_order = fields.Boolean(
        string='Is Coworking Space',
        compute = '_compute_is_space_order',
        store = True, precompute = True, readonly = False,
            # By default, all orders created in meter coworking space app are space Orders
        default = lambda self: self.env.context.get('in_meter_coworking_space_app')
    )
    has_space_products = fields.Boolean(compute='_compute_has_space_products')

    @api.depends('order_line.is_space')
    def _compute_has_space_products(self):
        for so in self:
            so.has_space_products = any(line.is_space for line in so.order_line)
    @api.depends('order_line.is_space')
    def _compute_is_space_order(self):
        for order in self:
            # If a rental product is added in the rental app to the order, it becomes a rental order
            order.is_space_order = order.is_space_order or order.has_space_products

    is_rental_order = fields.Boolean(
        string="Created In App Rental",
        compute='_compute_is_rental_order',
        store=True, precompute=True, readonly=False,
        # By default, all orders created in rental app are Rental Orders
        default=lambda self: self.env.context.get('in_rental_app'))