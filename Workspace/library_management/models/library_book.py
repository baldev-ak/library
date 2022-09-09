from odoo import api, fields, models

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "This model stores the data about the Book information "

    name = fields.Char(string = "Name")
    author = fields.Char(string = "Author")
    isbn_number = fields.Integer(string = "ISBN NUMBER")
    cover_photo = fields.Image(string = "Cover Photo")
    state = fields.Selection([
        ('good condition', 'Good Condition'),
        ('scrapped', 'Scrapped'),
        ], string = "state", default = "good condition")
    sale_history_ids = fields.One2many(comodel_name = "sale.history.book", inverse_name = "book_id", string = "Sales History")
    total_sum = fields.Float(string = "Total Sum", compute = "_compute_total_sum")

    def button_scrap(self):
        for rec in self:
            # print(rec.state,"-----------------\n\n\n")
            if rec.state == "good condition":
                rec.state = "scrapped"

    def _compute_total_sum(self):
        for rec in self:
            rec.total_sum = 0
            
            # total = self.env['sale.history.book'].search([('book_id','=',rec.id)])
            final_total = 0
            for result in rec.sale_history_ids:
                # print("\n\n----",result.visitor_id.name)
                final_total = result.subtotal + final_total

            rec.total_sum = final_total


    def action_total(self):
        print("\n\n\n----------------Clicked----------------\n\n\n")

class SalesHistoryBook(models.Model):
    _name = "sale.history.book"
    _description = "This model stores the data about the sales history of the Book"
    _rec_name = "visitor_id"

    book_id = fields.Many2one(comodel_name = "library.book", string = "Book")
    visitor_id = fields.Many2one(comodel_name = "visitor.visitor", string = "Visitor Name")
    quantity = fields.Integer(string = "Quantity")
    price = fields.Float(string = "Price")
    subtotal = fields.Float(string = "Sub Total", compute = "_compute_subtotal")

    @api.depends('price','quantity')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = 0
            if rec.price and rec.quantity:
                rec.subtotal = rec.price * rec.quantity


    
    

