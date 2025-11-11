from odoo import models, fields

class VentasTotales(models.Model):
    _name = "ventas.totales"
    _description = "Ventas totales realizadas"


    valor = fields.Float(string="Valor de las ventas totales")

    