# -*- coding: utf-8 -*-
{
    'name': "l10n_cl_dte_export",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_cl_invoice','l10n_cl_dte', 'account', 'account_accountant', 'product',],

    # always loaded
    'data': [
        #'data/desembarque.csv',
        #'data/embarque.csv',
        #'data/clausula.csv',
        #'data/moneda_export.csv',
        #'data/incoming_country.csv',
        #'data/outgoing_country.csv',
        #'data/modalidad.csv',
        #'data/forma_pago_export.csv',
        #'data/transporte.csv',
        #'data/paquete.csv',
        #'data/netweight.csv',
        #'data/weight.csv',
        'views/views.xml',
        'views/product_uom_categ.xml',
        'views/res_country.xml',
        'views/templates.xml',
        'views/sii_menuitem.xml',
        'views/sii_exportacion.xml',
        'views/account_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
