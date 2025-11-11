from odoo import models, fields

class EstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Propiedad Inmobiliaria"

    name = fields.Char(string="Nombre", required=True)
    price = fields.Float(string="Precio")
    active = fields.Boolean(string="Activo", default=True)

    _sql_constraints = [
        ('no_number_negative', 'CHECK(price >= 0)', "El numero esperado debe ser positivo"),
        ('name_not_null', 'CHECK(name IS NOT NULL)', "El nombre no puede estar vacio"),
        ('name_uniq', 'UNIQUE(name)',"El nombre de la clasificacion ya existe"),
    ] 