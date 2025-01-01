# -*- coding: utf-8 -*-
# from odoo import http


# class MaterialsManagement(http.Controller):
#     @http.route('/materials_management/materials_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/materials_management/materials_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('materials_management.listing', {
#             'root': '/materials_management/materials_management',
#             'objects': http.request.env['materials_management.materials_management'].search([]),
#         })

#     @http.route('/materials_management/materials_management/objects/<model("materials_management.materials_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('materials_management.object', {
#             'object': obj
#         })
