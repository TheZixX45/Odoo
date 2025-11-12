from odoo import models, fields, api

class Autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Autor de libros'
    
    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nacionalidad = fields.Char(string='Nacionalidad')
    biografia = fields.Text(string='Biografía')
    
    # Relación con libros (UN autor tiene MUCHOS libros)
    libro_ids = fields.One2many(
        'biblioteca.libro',  # Modelo relacionado
        'autor_id',          # Campo en el otro modelo
        string='Libros'      # Texto que verá el usuario
    )
    
    # Campo calculado - Cuántos libros tiene el autor
    total_libros = fields.Integer(
        string='Total de Libros',
        compute='_compute_total_libros'
    )
    
    @api.depends('libro_ids')
    def _compute_total_libros(self):
        for autor in self:
            autor.total_libros = len(autor.libro_ids)

            