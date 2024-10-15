# -*- coding: utf-8 -*-
{
    'name': "My Module",
    'version': '1.0',
    'category': 'Other',
    'summary': 'A simple Odoo module',
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/report.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,

    'assets': {
        'web.assets_backend': ['my_module/static/src/js/button.js'],
    },
}

