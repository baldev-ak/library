# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library Management',
    'version' : '1.0',
    'summary': 'Library Management',
    'sequence': 0,
    'description': """Library Management""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['base_setup'],
    'data': [
    'security/ir.model.access.csv',
    'views/library_view.xml',
    'views/librarian_view.xml',
    'views/visitor_view.xml',
    'views/library_book_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
