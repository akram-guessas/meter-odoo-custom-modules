from odoo import models, fields, api

class MTRFloor(models.Model):
    _name = 'mtr_coworking.floor'
    _description = 'Floor Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    type = fields.Selection([
        ('private', 'Private'),
        ('coworking_space', 'CoWorking Space')
    ], string='Type', required=True)
    floor_capacity = fields.Integer(string='Capacity')
    # building_id = fields.Many2one(
    #     comodel_name='mtr_coworking.building', string='Building', required=True
    # )
    # office_ids = fields.One2many(
    #     comodel_name='mtr_coworking.office', inverse_name='floor_id', string='Offices'
    # )

    # space_ids = fields.One2many(
    #     comodel_name='product.template', inverse_name='floor_id', string='Product'
    # )

    space_ids = fields.One2many(
        comodel_name='product.template',
        inverse_name='floor_id',
        string='Coworking Spaces',
        # compute='_compute_space_ids',
        readonly=True
    )

    # @api.depends('space_ids.is_coworking_space')
    # def _compute_space_ids(self):
    #     for floor in self:
    #         floor.space_ids = self.env['product.template'].search([
    #             ('floor_id', '=', floor.id),
    #             ('is_coworking_space', '=', True)
    #         ])


    num_spaces = fields.Integer(
        string='Number of Spaces', compute='_compute_space_ids', store=True
    )

    @api.depends('space_ids')
    def _compute_space_ids(self):
        for record in self:
            record.num_spaces = len(record.space_ids)
