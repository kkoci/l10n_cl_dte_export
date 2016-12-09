# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import fields as old_fields
from openerp.exceptions import except_orm, Warning
import openerp.addons.decimal_precision as dp

class embarque(models.Model):
    _name = 'embarque'
    _rec_name = 'shipment_port'

    code_embarque = fields.Integer(string="Código")
    shipment_port = fields.Char(string="Puerto de embarque")

class forma_pago_export(models.Model):
    _name = 'forma_pago_export'
    _rec_name = 'forma_p_export'

    code_forma_pago = fields.Integer(string="Código")
    forma_p_export = fields.Char(string="Forma de pago Exportación")

class desembarque(models.Model):
    _name = 'desembarque'
    _rec_name = 'landing_port'

    code_desembarque = fields.Integer(string="Código")
    landing_port = fields.Char(string="Puerto de desembarque")

class transporte(models.Model):
    _name = 'transporte'
    _rec_name = 'via_transport'

    code_transporte = fields.Integer(string="Código")
    via_transport = fields.Char(string="Vía de Transporte")

class clausula(models.Model):
    _name = 'clausula'
    _rec_name = 'clausule'

    code_clausula = fields.Integer(string="Código")
    clausule = fields.Char(string="Cláusula de Venta")

class paquete(models.Model):
    _name = 'paquete'
    _rec_name = 'package_type'

    code_paquete = fields.Integer(string="Código")
    package_type = fields.Char(string="Tipo de Bulto")

class modalidad(models.Model):
    _name = 'modalidad'
    _rec_name = 'modality'

    code_modalidad = fields.Integer(string="Código")
    modality = fields.Char(string="Modalidad de Venta")

class tipo_tara(models.Model):
    _name = 'tipo_tara'
    _rec_name = 'tara_unidad'

    code_tara = fields.Integer(string="Código")
    tara_unidad = fields.Integer(string="Unidad de medida de Tara")

class weight(models.Model):
    _name = 'weight'
    _rec_name = 'weight_unidad'

    code_weight = fields.Integer(string="Código")
    weight_unidad = fields.Char(string="Unidad de peso bruto")

class servicio(models.Model):
    _name = 'servicio'
    _rec_name = 'servicio'

    code_servicio = fields.Integer(string="Código del Servicio")
    servicio = fields.Char(string="Servicio")

class netweight(models.Model):
    _name = 'netweight'
    _rec_name = 'net_weight_unidad'

    code_netweight = fields.Integer(string="Código")
    net_weight_unidad = fields.Char(string="Unidad de peso neto")

class forma_pago_export(models.Model):
    _name = 'forma_pago_export'
    _rec_name = 'fma_pago_export'

    code_fma_pago_export = fields.Integer(string="Código forma pago exportación")
    fma_pago_export = fields.Char(string="Forma pago de exportación")

class product_uom_categ(models.Model):
    _inherit = 'product.uom.categ'

    code_product = fields.Char(string="Código Unidad")

class Currency(models.Model):
    _name = 'res.currency'
    _inherit = 'res.currency'

    code_currency = fields.Integer(string="Código de la moneda")

class country(models.Model):
    _name = 'res.country'
    _inherit = 'res.country'

    iso_code = fields.Integer(string="Código del País, para exportación")

class paymentTerm(models.Model):
    _inherit = 'account.payment.term'

    dte_sii_code = fields.Selection(selection_add=[('4', 'COB1'),
        ('5','COBRANZA'),
        ('11','ACRED'),
        ('12','CBOF'),
        ('21','S/PAGO'),
        ('32','ANTICIPO')])

class account_invoice(models.Model):
    _inherit = "account.invoice"

    #def _is_export(self):
        #if self.sii_document_class_id.sii_code in [110, 111, 112]:
            #return True
        #return False
    #es_boleta = inv._es_boleta()

    is_export = fields.Boolean(string="¿Es exportación?", default=False)
    #IdDoc
    despacho_tipo = fields.Selection([
        ('1','Despacho por Cuenta del Comprador'),
        ('2','Despacho por Cuenta del Emisor a Instalaciones del Comprador'),
        ('3','Despacho por Cuenta del Emisor a Otras Instalaciones')], string="Tipo de despacho", readonly=True, states={'draft': [('readonly', False)]})
    es_servicio = fields.Many2one(comodel_name="servicio", string="Es una factura por servicio")
    #payment_forma = fields.Many2one(comodel_name="forma_pago_export", string="Forma de Pago exportación")
    forma_de_pago_export = fields.Many2one(comodel_name="fma_pago_export", string="Forma pago de exportación")
    fecha_cancelacion = fields.Date(string="Fecha de Cancelacion del DTE")
    monto_cancelado = fields.Float(string="Monto Cancelado al emitirse el documento", help="Monto Cancelado al emitirse el documento")
    saldo_insoluto = fields.Float(string="Saldo Insoluto al emitirse el documento")
    fecha_pago = fields.Date(string="Fecha de pago")
    monto_pago = fields.Float(string="Monto pago")
    glosa = fields.Many2one(
        'sii.activity.description',
        string='Glosa de pago', ondelete="restrict")
    periodo_desde = fields.Date(string="Período desde")
    periodo_hasta = fields.Date(string="Período hasta")
    medio_pago = fields.Char(string="Medio de pago")
    tipo_cuenta_pago = fields.Char(string="Tipo cuenta pago")
    numero_cta_pago = fields.Char(string="Numero cuenta pago")
    banco_pago = fields.Many2one('res.bank', 'Banco donde se realizo el pago', readonly=True)
    termino_de_pago = fields.Char(string="Término del pago")
    termino_pago_glosa = fields.Many2one(
       'sii.activity.description',
        string="Glosa correspondiente al Término de pago",
        related="partner_id.activity_description",
        readonly=True,
    )
    dias_termino_pago = fields.Integer(string="Dias del termino de pago")
    fecha_vencimiento = fields.Date(string="Fecha de vencimiento término")
    #Transporte
    vehicle = fields.Many2one('fleet.vehicle', string="Vehículo", readonly=False, states={'done':[('readonly',True)]})
    chofer= fields.Many2one('res.partner', string="Chofer", readonly=False, states={'done':[('readonly',True)]})
    patente = fields.Char(string="Patente", readonly=False, states={'done':[('readonly',True)]})
    #Aduana
    modal_idad = fields.Many2one(comodel_name="modalidad", string="Modalidad de Venta")
    clau_sula = fields.Many2one(comodel_name="clausula", string="Clausula")
    total_clausule = fields.Float(string="Total cláusula de Venta")
    transporte_tipo = fields.Many2one(comodel_name="transporte", string="Vía de transporte")
    booking = fields.Char(string="Booking", help="Numero de reserva del Operador")
    puerto_embarque = fields.Many2one(comodel_name="embarque", string="Puerto de Embarque")
    puerto_desembarque = fields.Many2one(comodel_name="desembarque", string="Puerto de Desembarque")
    tara = fields.Float(string="Tara")
    tara_unit = fields.Many2one(comodel_name="product.uom.categ", string="Unidad de medida de Tara")
    weight = fields.Float(string="Peso Bruto")
    weight_unit = fields.Many2one(comodel_name="product.uom.categ", string="Unidad de peso bruto")
    neto = fields.Float(string="Peso Neto")
    net_weight_unit = fields.Many2one(comodel_name="product.uom.categ", string="Unidad de peso neto")
    tot_items = fields.Integer(string="Total Items")
    tot_bultos = fields.Integer(string="Total Bultos")
    monto_flete = fields.Float(string="Monto Flete")
    monto_seguro = fields.Float(string="Seguro")
    receiving_country = fields.Many2one(comodel_name="res.country", string="País receptor")
    destination_country = fields.Many2one(comodel_name="res.country", string="País destino")
    #Bultos
    type_package = fields.Many2one(comodel_name="paquete", string="Tipo de Bulto")
    cant_bultos = fields.Integer(string="Cantidad Bultos")
    marcas = fields.Char(string="Marcas", help="Identificación de marcas, cuando es distinto de contenedor")
    id_container = fields.Char(string="Id Container", help="Se utiliza cuando el tipo de bulto es contenedor")
    sello = fields.Char(string="Sellos", help="Sello contenedor. Con digito verificador")
    emisor_sello = fields.Many2one(comodel_name="res.partner", string="Emisor Sellos")
    #Otramoneda
    moneda_export = fields.Many2one(comodel_name='res.currency', string="Moneda de la exportación")
    tipo_cambio = fields.Float(string="Tipo de cambio")
    monto_exe_export = fields.Float(string="Monto exento exportación")
    total_export_moneda = fields.Float(string="Monto total en moneda extranjera")
    #emisor = fields.Many2one
    #codigo_vendedor = fields.Char
    #id_adicional_vendedor = fields.Char
    #receptor = fields.Many2one
    #id_receptor_extranjero = fields.Many2one
    #nacionalidad = fields.Many2one
    #id_adicional_receptor_extranjero = fields.Char
    #freight_price = fields.Float(string="Flete")
    #assurance_total = fields.Float(string="Seguro")
    #contact_id = fields.Many2one('res.partner',string="Contacto", readonly=False, states={'done':[('readonly',True)]})

    @api.onchange('vehicle')
    def _setChofer(self):
        self.chofer = self.vehicle.driver_id
        self.patente = self.vehicle.license_plate

    @api.onchange('carrier_id')
    def _setChoferFromCarrier(self):
        self.chofer = self.carrier_id.partner_id    

class stock_picking(models.Model):
    _inherit = 'stock.picking'