from odoo import models, fields, api

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de la biblioteca'
    
    name = fields.Char(string='Título', required=True)
    isbn = fields.Char(string='ISBN')
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    paginas = fields.Integer(string='Número de Páginas')
    precio = fields.Float(string='Precio')
    
    # ★ RELACIÓN IMPORTANTE ★ (MUCHOS libros pertenecen a UN autor)
    autor_id = fields.Many2one(
        'biblioteca.autor',  # Modelo relacionado
        string='Autor',      # Texto que verá el usuario
        required=True        # ★ Todo libro DEBE tener autor
    )
    
    # Campo relacionado (a través del autor)
    nacionalidad_autor = fields.Char(
        string='Nacionalidad del Autor',
        related='autor_id.nacionalidad',
        readonly=True
    )