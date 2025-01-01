from sqlite3 import apilevel
from xml.dom import ValidationErr
from odoo import models, fields
import re

class Supplier(models.Model):
    _name = 'material.management.supplier'
    _description = 'Supplier'
    
    nama = fields.Char(string='Nama', required=True)
    alamat = fields.Text(string='Alamat')
    phone = fields.Char(string='Phone')
    
    from odoo import api

    @api.constrains('phone')
    def _check_phone_number(self):

        pass

        for record in self:
            if record.phone and not re.match(r'^\d{10,15}$', record.phone):
                raise ValidationErr("Phone number must be between 10 and 15 digits.")
