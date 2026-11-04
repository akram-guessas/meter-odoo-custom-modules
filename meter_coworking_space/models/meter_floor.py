from odoo import api, fields, models


class CoworkingFloor(models.Model):
    _name = "mtr_coworking.floor"
    _description = "Coworking Floor"
    _order = "name"

    name = fields.Char(required=True)
    description = fields.Text()
    type = fields.Selection(
        [("private", "Private"), ("coworking_space", "Coworking Space")],
        required=True,
        default="coworking_space",
    )
    floor_capacity = fields.Integer(string="Capacity")
    space_ids = fields.One2many(
        comodel_name="product.template",
        inverse_name="floor_id",
        string="Spaces",
        readonly=True,
    )
    num_spaces = fields.Integer(
        string="Number of Spaces", compute="_compute_num_spaces", store=True
    )

    @api.depends("space_ids")
    def _compute_num_spaces(self):
        for floor in self:
            floor.num_spaces = len(floor.space_ids)
