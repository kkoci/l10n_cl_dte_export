# -*- coding: utf-8 -*-
from openerp import http

# class L10nClDteExport(http.Controller):
#     @http.route('/l10n_cl_dte_export/l10n_cl_dte_export/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_dte_export/l10n_cl_dte_export/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_dte_export.listing', {
#             'root': '/l10n_cl_dte_export/l10n_cl_dte_export',
#             'objects': http.request.env['l10n_cl_dte_export.l10n_cl_dte_export'].search([]),
#         })

#     @http.route('/l10n_cl_dte_export/l10n_cl_dte_export/objects/<model("l10n_cl_dte_export.l10n_cl_dte_export"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_dte_export.object', {
#             'object': obj
#         })