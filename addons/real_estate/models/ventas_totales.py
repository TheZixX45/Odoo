from odoo import models, fields

class VentasTotales(models.Model):
    _name = "ventas.totales"
    _description = "Ventas totales realizadas"


    valor = fields.Float(string="Valor de las ventas totales")

    _sql_constraints = [
        ('name_not_null', 'CHECK(valor IS NOT NULL)', "El nombre no puede estar vacio"),
        ('no_number_negative', 'CHECK(valor >= 0)', "El numero esperado debe ser positivo"),
        ('name_uniq', 'UNIQUE(valor)',"El nombre de la clasificacion ya existe"),
    ] 