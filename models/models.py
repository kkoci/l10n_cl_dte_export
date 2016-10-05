# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, Warning
import openerp.addons.decimal_precision as dp

class account_invoice(models.Model):
    _inherit = "account.invoice"

    currency_id = fields.Many2one('res.currency', string="Moneda de la exportación")
    #forma_pago = fields.Many2one('forma_pago')
    modality = fields.Char(string="Modalidad de Venta")
    clausule = fields.Char(string="Cláusula de Venta")
    total_clausule = fields.Float(string="Total cláusula de Venta")
    via_transport = fields.Char(string="Vía de Transporte")
    shipment_port = fields.Char(string="Puerto de embarque")
    landing_port = fields.Char(string="Puerto de desembarque")
    tara_unit = fields.Char(string="Unidad de medida de Tara")
    weight_unit = fields.Char(string="Unidad de peso bruto")
    net_weight_unit = fields.Char(string="Unidad de peso neto")
    package_type = fields.Char(string="Tipo de Bulto")
    package_total = fields.Integer(string="Total Bultos")
    freight_price = fields.Float(string="Flete")
    assurance_total = fields.Float(string="Seguro")
    receiving_country = fields.Many2one('res.country', string="País receptor")
    destination_country = fields.Many2one('res.country', string="País destino")