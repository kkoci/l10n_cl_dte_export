# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, Warning
import openerp.addons.decimal_precision as dp

class embarque(models.Model):
    _name = 'embarque'
    _rec_name = 'shipment_port'

    #forma_pago = fields.Many2one('forma_pago')
    shipment_port = fields.Char(string="Puerto de embarque")

class desembarque(models.Model):
    _name = 'desembarque'
    _rec_name = 'landing_port'

    landing_port = fields.Char(string="Puerto de desembarque")

class transporte(models.Model):
    _name = 'transporte'
    _rec_name = 'via_transport'

    via_transport = fields.Char(string="Vía de Transporte")

class clausula(models.Model):
    _name = 'clausula'
    _rec_name = 'clausule'

    clausule = fields.Char(string="Cláusula de Venta")

class paquete(models.Model):
    _name = 'paquete'
    _rec_name = 'package_type'

    package_type = fields.Char(string="Tipo de Bulto")

class modalidad(models.Model):
    _name = 'modalidad'
    _rec_name = 'modality'

    modality = fields.Char(string="Modalidad de Venta")

class tara(models.Model):
    _name = 'tara'
    _rec_name = 'tara_unidad'

    tara_unidad = fields.Char(string="Unidad de medida de Tara")

class weight(models.Model):
    _name = 'weight'
    _rec_name = 'weight_unidad'

    weight_unidad = fields.Char(string="Unidad de peso bruto")

class netweight(models.Model):
    _name = 'netweight'
    _rec_name = 'net_weight_unidad'

    net_weight_unidad = fields.Char(string="Unidad de peso neto")

class account_invoice(models.Model):
    #_inherit = ["account.invoice", "product.uom"]
    _inherit = "account.invoice"

    puerto_embarque = fields.Many2one(comodel_name="embarque", string="Puerto de Embarque")
    puerto_desembarque = fields.Many2one(comodel_name="desembarque", string="Puerto de Desembarque")
    moneda_export = fields.Many2one(comodel_name='res.currency', string="Moneda de la exportación")
    modal_idad = fields.Many2one(comodel_name="modalidad", string="Modalidad")
    type_package = fields.Many2one(comodel_name="paquete", string="Tipo de Paquete")
    clau_sula = fields.Many2one(comodel_name="clausula", string="Clausula")
    transporte_tipo = fields.Many2one(comodel_name="transporte", string="Vía de transporte")
    freight_price = fields.Float(string="Flete")
    receiving_country = fields.Many2one('res.country', string="País receptor")
    destination_country = fields.Many2one('res.country', string="País destino")
    package_total = fields.Integer(string="Total Bultos")
    assurance_total = fields.Float(string="Seguro")
    total_clausule = fields.Float(string="Total cláusula de Venta")
    tara_unit = fields.Many2one(comodel_name="tara", string="Unidad de medida de Tara")
    weight_unit = fields.Many2one(comodel_name="weight", string="Unidad de peso bruto")
    net_weight_unit = fields.Many2one(comodel_name="netweight", string="Unidad de peso neto")
    #tara_unit = fields.Char(string="Unidad de medida de Tara")
    #weight_unit = fields.Char(string="Unidad de peso bruto")
    #net_weight_unit = fields.Char(string="Unidad de peso neto")



