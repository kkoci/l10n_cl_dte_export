# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, Warning
import openerp.addons.decimal_precision as dp

class embarque(models.Model):
    _name = 'embarque'
    #_inherit = "account.invoice"
    _rec_name = 'shipment_port'

    #forma_pago = fields.Many2one('forma_pago')
    modality = fields.Char(string="Modalidad de Venta")
    clausule = fields.Char(string="Cláusula de Venta")
    via_transport = fields.Char(string="Vía de Transporte")
    shipment_port = fields.Char(string="Puerto de embarque")
    tara_unit = fields.Char(string="Unidad de medida de Tara")
    weight_unit = fields.Char(string="Unidad de peso bruto")
    net_weight_unit = fields.Char(string="Unidad de peso neto")
    package_type = fields.Char(string="Tipo de Bulto")

class desembarque(models.Model):
    _name = 'desembarque'
    #_inherit = "account.invoice"
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")

'''class desembarque(models.Model):
    _name = 'desembarque'
    #_inherit = "account.invoice"
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")

class desembarque(models.Model):
    _name = 'desembarque'
    #_inherit = "account.invoice"
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")'''

'''class desembarque(models.Model):
    _name = 'desembarque'
    #_inherit = "account.invoice"
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")

class desembarque(models.Model):
    _name = 'desembarque'
    #_inherit = "account.invoice"
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")'''

class account_invoice(models.Model):
    _inherit = "account.invoice"

    puerto_embarque = fields.Many2one(comodel_name="embarque", string="Puerto de Embarque")
    puerto_desembarque = fields.Many2one(comodel_name="desembarque", string="Puerto de Desembarque")
    freight_price = fields.Float(string="Flete")
    receiving_country = fields.Many2one('res.country', string="País receptor")
    destination_country = fields.Many2one('res.country', string="País destino")
    package_total = fields.Integer(string="Total Bultos")
    assurance_total = fields.Float(string="Seguro")
    total_clausule = fields.Float(string="Total cláusula de Venta")
    moneda_export = fields.Many2one('res.currency', string="Moneda de la exportación")


