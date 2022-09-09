from odoo import api, fields, models
from datetime import date

class Librarian(models.Model):
    _name = "librarian.librarian"
    _description = "This is master Table to store the Librarians"

    name = fields.Char(string = "Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ], string = "Gender")
    DOB = fields.Date(string = "DOB")
    age = fields.Integer(string = "Age", compute = "_compute_age")
    date_of_joining = fields.Date(string = "Date of Joining")
    current_experience = fields.Float(string = "Current Experience", compute = "_compute_experience")   

    @api.depends('DOB')
    def _compute_age(self):
        for rec in self:
            rec.age = 0

            if rec.DOB:
                today = date.today()
                dob = rec.DOB
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                rec.age = age

    @api.depends('date_of_joining')
    def _compute_experience(self):
        for rec in self:
            rec.current_experience = 0 
            if rec.date_of_joining:
                today = date.today()
                doj = rec.date_of_joining
                exp = today.year - doj.year - ((today.month, today.day) < (doj.month, doj.day))
                rec.current_experience = exp
