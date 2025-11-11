from odoo import models, fields

class EstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Propiedad Inmobiliaria"

    name = fields.Char(string="Nombre", required=True)
    price = fields.Float(string="Precio")
    active = fields.Boolean(string="Activo", default=True)
