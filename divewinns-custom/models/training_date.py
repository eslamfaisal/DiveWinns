from odoo import api, models, fields

class TrainingDate(models.Model):
    _name = "divewinns.training.date"
    _description = "Date of training"

    name = fields.Char(string="Name", required=True)
    date = fields.Datetime(string="Date", required=True)
    
    event_id = fields.Many2one(comodel_name="event.event", string="Event")
    calendar_event_id = fields.Many2one(comodel_name="calendar.event", string="Calendar event")

    organizer_id = fields.Many2one(comodel_name="res.users", string="Organizer", required=True)
    partner_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    @api.model
    def create(self, vals):
        obj = super(TrainingDate, self).create(vals)
        calendar_event = self.env["calendar.event"].create({
            "name": obj.name,
            "start": obj.date,
            "stop": obj.date,
            "allday": True,
            "user_id": obj.organizer_id.id,
            "partner_ids": obj.partner_ids,
        })
        obj.calendar_event_id = calendar_event.id
        return obj

    @api.onchange('date')
    def _on_date_changed(self):
        for training_date in self:
            training_date.calendar_event_id.start = training_date.date

    