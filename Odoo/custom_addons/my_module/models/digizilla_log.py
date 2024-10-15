from odoo import models, fields


class DigizillaLog(models.Model):
    _name = 'digizilla.log'
    _description = 'Digizilla Change Log'

    digizilla_id = fields.Many2one('digizilla.model', string="Digizilla", required=True)
    field_name = fields.Char(string="Field Name")
    old_value = fields.Char(string="Old Value")
    new_value = fields.Char(string="New Value")
    change_date = fields.Datetime(string="Change Date", default=fields.Datetime.now)
