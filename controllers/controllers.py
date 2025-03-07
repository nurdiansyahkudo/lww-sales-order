# -*- coding: utf-8 -*-
# from odoo import http


# class LwwSales(http.Controller):
#     @http.route('/lww_sales/lww_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lww_sales/lww_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lww_sales.listing', {
#             'root': '/lww_sales/lww_sales',
#             'objects': http.request.env['lww_sales.lww_sales'].search([]),
#         })

#     @http.route('/lww_sales/lww_sales/objects/<model("lww_sales.lww_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lww_sales.object', {
#             'object': obj
#         })

