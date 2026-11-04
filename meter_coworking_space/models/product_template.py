from odoo import Command, api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    space_ok = fields.Boolean(
        string="Is Coworking Space",
        help="Check this box if customers can book this product as a coworking space.",
    )
    floor_id = fields.Many2one(comodel_name="mtr_coworking.floor", string="Floor")

    @api.onchange("space_ok")
    def _onchange_space_ok(self):
        category = self.env.ref(
            "meter_coworking_space.coworking_category", raise_if_not_found=False
        )
        if not category:
            return
        for product in self.filtered("space_ok"):
            product.public_categ_ids = [Command.link(category.id)]
