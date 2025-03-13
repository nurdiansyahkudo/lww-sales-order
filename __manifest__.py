# -*- coding: utf-8 -*-
{
    'name': "Limawira Sales Order",
    'summary': '',
    'author': '',
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        # SALES ORDER
        'report/lww_sales_report.xml',
        'views/lww_so_template.xml',
        'views/bs_so_template.xml',
        # 'views/spartadua_so_template.xml',
        # FORM VIEW
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}

