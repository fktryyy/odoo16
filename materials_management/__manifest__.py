{
    'name': 'Material Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'modul ini di gunakan untuk management materials dan suppliers',
    'author': 'Dimas Dewandaru Sebastian',
    'depends': ['base', 'stock'],
    'data': [
        'views/material_views.xml',
        'views/supplier_views.xml',
    ],
    'installable': True,
    'application': True,
}
