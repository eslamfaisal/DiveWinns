from odoo import api, models, fields

class TrainingDate(models.Model):
    _name = "divewinns.training.date"
    _description = "Date of training"

    name = fields.Char(string="Name", required=True, default=lambda self: self.event_id.name)
    start = fields.Datetime(string="Start Date", required=True)
    end = fields.Datetime(string="End Date", required=True)
    description = fields.Text(string="Description", required=True)
    room = fields.Selection(string="Room", required=True, selection=[("training1", "Trainingsroom 1"), ("training2", "Trainingsroom 2"), ("community", "Community"), ("pool", "Pool"), ("bus", "Bus")])
    
    event_id = fields.Many2one(comodel_name="event.event", string="Event")
    calendar_event_id = fields.Many2one(comodel_name="calendar.event", string="Calendar event")

    organizer_id = fields.Many2one(comodel_name="res.users", string="Organizer", required=True, default=lambda self: self.event_id.instructor_id.user_id)
    #partner_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")



    @api.model
    def create(self, vals):
        obj = super(TrainingDate, self).create(vals)
        alarm_id = self.env["calendar.alarm"].search([('alarm_type', '=', 'email'), ('duration', '=', 1), ('interval', '=', 'days')])
        if not alarm_id:
            alarm_id = self.env["calendar.alarm"].create({
                'name': "E-mail 1 Day",
                'alarm_type': 'email',
                'duration': 1,
                'interval': 'days',
            })
        calendar_event = self.env["calendar.event"].create({
            "name": obj.name,
            "start": obj.start,
            "stop": obj.end,
            "user_id": obj.organizer_id.id,
            "event_id": obj.event_id,
            "partner_ids": obj.event_id.registration_ids.partner_id,
            "alarm_ids": [(4, alarm_id)]
        })
        calendar_event.partner_ids = [(4, obj.organizer_id.partner_id.id)]
        obj.calendar_event_id = calendar_event.id
        return obj

    @api.onchange('start', 'end')
    def _on_date_changed(self):
        for training_date in self:
            training_date.calendar_event_id.start = training_date.start
            training_date.calendar_event_id.stop = training_date.end

    