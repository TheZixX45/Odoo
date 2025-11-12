{
    'name': 'Biblioteca',
    'version': '1.0',
    'depends': ['base'],
    'description': """Módulo creado con fines de aprender jeje""",
    'summary': 'Modulo para una biblioteca',
    'category': 'Tools',
    'sequence': 50,
    'data': [
        'security/ir.model.access.csv',
        'views/autores_views.xml',
        'views/libros_views.xml',
        'views/menu_biblioteca.xml'        
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
