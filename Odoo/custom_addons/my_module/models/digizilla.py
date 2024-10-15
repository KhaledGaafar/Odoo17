from odoo import models, fields,api

class Digizilla(models.Model):
    _name = 'digizilla.model'
    _description = 'Digizilla'

    name = fields.Char(required=True)
    gender = fields.Selection([('male', 'Male')])
    country = fields.Char()
    joining_date = fields.Date()
    tags = fields.Many2many('res.partner.category', string='Tags')
    customers = fields.Many2many('res.partner', string='Customers')
    company = fields.Many2one('res.company', required=True)
    notes = fields.Text()
    comments = fields.Char()
    log_ids = fields.One2many('digizilla.log', 'digizilla_id', string="Change Logs")


    
    @api.model
    def create(self, vals):
        record = super(Digizilla, self).create(vals)
        self._log_changes(record, vals, 'create')
        return record

    def write(self, vals):
        self._log_changes(self, vals, 'write')
        return super(Digizilla, self).write(vals)

    def _log_changes(self, records, vals, operation):
        log_model = self.env['digizilla.log']
        for record in records:
            for field, new_value in vals.items():
                old_value = record[field]
                log_model.create({
                    'digizilla_id': record.id,
                    'field_name': field,
                    'old_value': old_value,
                    'new_value': new_value,
                    'change_date': fields.Datetime.now(),
                })





