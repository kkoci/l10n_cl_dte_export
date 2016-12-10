# -*- coding: utf-8 -*-
from openerp import fields, models, api, _


class partner(models.Model):
    '''
    Stuff for export
    '''
    _name = 'res.partner'
    _inherit = 'res.partner'

    #Export
    direccion_postal = fields.Char(string="Direccion postal")
    comuna_postal = fields.Char(string="Comuna Postal")
    ciudad_postal = fields.Char(string="Ciudad Postal")
    codigo_interno_receptor = fields.Char(string="Código interno Receptor")
    codigo_vendedor = fields.Char(string="Codigo si es vendedor")
    identificacion_adicional_vendedor = fields.Char(string="Identificacion adicional de vendedor")
    identificacion_adicional_transporte = fields.Char(string="Identificaćion adicional si es un transporte")
    es_operador = fields.Boolean(string="¿Es un operador aduanal?", default=False)
    nombre_operador = fields.Char(string="Nombre del operador")
    codigo_operador = fields.Char(string="Código del operador")
    es_extranjero = fields.Boolean(string="¿Es extranjero?", default=False)
    identificacion_extranjero = fields.Char(string="Identificacion")
    nacionalidad = fields.Many2one(comodel_name="res.country", string="Nacionalidad")
    identificacion_adicional_extranjero = fields.Char(string="Id adicional extranjero")