from odoo import api, fields, models

class Visitor(models.Model):
    _name = "visitor.visitor"
    _description = "This stores data of Visitor "

    name = fields.Char(string = "Name")