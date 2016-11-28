# -*- coding: utf-8 -*-
from openerp import osv, models, fields, api, _
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, UserError
import openerp.addons.decimal_precision as dp

class Country(models.Model):
	_name = 'res.country'
    _inherit = 'res.country'

    'iso_code' = fields.Integer(string="Código del País, para exportación")