from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.management.material'
    _description = 'Material'
    
    kode = fields.Char(string='Kode', required=True, unique=True)
    nama = fields.Char(string='Nama', required=True)
    tipe_material = fields.Selection(
        [('consumable', 'Consumable'), ('stockable', 'Stockable'), ('service', 'Service')],
        string='Tipe Material', required=True
    )
    buy_price = fields.Float(string='Buy Price', required=True)
    supplier_id = fields.Many2one('material.management.supplier', string='Supplier', required=True)
    
    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy Price cannot be less than 100.")
