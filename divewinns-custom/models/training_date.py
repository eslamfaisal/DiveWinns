from odoo import api, models, fields

class TrainingDate(models.Model):
    _name = "divewinns.training.date"

    name = fields.Char(string="Name")
    date = fields.Datetime(string="Date", required=True)
    
    event_id = fields.Many2one(comodel_name="event.event", string="Event")
    calendar_event_id = fields.Many2one(comodel_name="calendar.event", string="Calendar event")

    organizer_id = fields.Many2one(comodel_name="res.partner", string="Organizer", required=True)
    partner_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    @api.model
    def create(self, vals):
        obj = super(TrainingDate, self).create(vals)
        # TODO: Create calendar event
        return obj

    