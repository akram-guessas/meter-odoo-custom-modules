from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    is_space = fields.Boolean(related="product_id.space_ok", store=True)
    space_start = fields.Datetime(string="Booking Start")
    space_end = fields.Datetime(string="Booking End")
    space_duration = fields.Float(
        string="Duration (Hours)", compute="_compute_space_duration", store=True
    )

    @api.depends("space_start", "space_end")
    def _compute_space_duration(self):
        for line in self:
            if line.space_start and line.space_end and line.space_end > line.space_start:
                delta = line.space_end - line.space_start
                line.space_duration = delta.total_seconds() / 3600
            else:
                line.space_duration = 0.0

    @api.constrains("space_start", "space_end")
    def _check_space_dates(self):
        for line in self:
            if line.space_start and line.space_end and line.space_end <= line.space_start:
                raise ValidationError(
                    self.env._("The booking end must be after the booking start.")
                )

    @api.onchange("space_start", "space_end")
    def _onchange_space_dates(self):
        for line in self.filtered(lambda l: l.is_space and l.space_duration):
            line.product_uom_qty = line.space_duration

    def _check_space_availability(self):
        """Block a booking when the same space is already booked for an overlapping period."""
        for line in self.filtered("is_space"):
            if not (line.space_start and line.space_end):
                raise UserError(
                    self.env._(
                        "Set the booking start and end for %(space)s.",
                        space=line.product_id.display_name,
                    )
                )
            overlap = self.search_count([
                ("id", "!=", line.id),
                ("product_id", "=", line.product_id.id),
                ("space_start", "<", line.space_end),
                ("space_end", ">", line.space_start),
                "|",
                ("order_id.state", "=", "sale"),
                ("order_id", "=", line.order_id.id),
            ], limit=1)
            if overlap:
                raise ValidationError(
                    self.env._(
                        "%(space)s is already booked between %(start)s and %(end)s.",
                        space=line.product_id.display_name,
                        start=fields.Datetime.to_string(line.space_start),
                        end=fields.Datetime.to_string(line.space_end),
                    )
                )
