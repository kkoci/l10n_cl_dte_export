# -*- coding: utf-8 -*-

from openerp import fields, models, api, _
from openerp.exceptions import UserError
from datetime import datetime, timedelta
import logging
from lxml import etree
from lxml.etree import Element, SubElement
from openerp import SUPERUSER_ID

import xml.dom.minidom
import pytz


import socket
import collections

class invoice(models.Model):
    _inherit = "account.invoice"

    def _id_doc_2(self, taxInclude=False, MntExe=0):
        IdDoc= collections.OrderedDict()
        IdDoc['TipoDTE'] = self.sii_document_class_id.sii_code
        IdDoc['Folio'] = self.get_folio()
        IdDoc['FchEmis'] = self.date_invoice
        if self._es_boleta():
            IdDoc['IndServicio'] = 3 #@TODO agregar las otras opciones a la fichade producto servicio
        if not self._es_boleta():
            IdDoc['TpoImpresion'] = "N" #@TODO crear opcion de ticket
        #if self.tipo_servicio:
        #    Encabezado['IdDoc']['IndServicio'] = 1,2,3,4
        # todo: forma de pago y fecha de vencimiento - opcional
        if taxInclude and MntExe == 0 and not self._es_boleta():
        	IdDoc['MntBruto'] = 1
        if not self._es_boleta():
            IdDoc['FmaPago'] = self.forma_pago or 1
        if not taxInclude and self._es_boleta():
        	IdDoc['IndMntNeto'] = 2
        #if self._es_boleta():
            #Servicios periódicos
        #    IdDoc['PeriodoDesde'] =
        #    IdDoc['PeriodoHasta'] =
        if not self._es_boleta():
            IdDoc['FchVenc'] = self.date_due or datetime.strftime(datetime.now(), '%Y-%m-%d')
        return IdDoc

    '''def _idDoc(self):
        IdDoc = super(tuclase,self)._idDoc()
        New = ordered.collections()
        For key,value in iddoc.iteritems():
        If key == "target":
            New['indservicio'] = 3
            New[key] = value

        return new'''

    def _dte_2(self, n_atencion=None):
        dte = collections.OrderedDict()
        invoice_lines = self._invoice_lines()
        dte['Encabezado'] = self._encabezado(invoice_lines['MntExe'], invoice_lines['no_product'], invoice_lines['tax_include'])
        lin_ref = 1
        ref_lines = []
        if self.company_id.dte_service_provider == 'SIIHOMO' and isinstance(n_atencion, unicode) and not self._es_boleta():
            ref_line = {}
            ref_line = collections.OrderedDict()
            ref_line['NroLinRef'] = lin_ref
            ref_line['TpoDocRef'] = "SET"
            ref_line['FolioRef'] = self.get_folio()
            ref_line['FchRef'] = datetime.strftime(datetime.now(), '%Y-%m-%d')
            ref_line['RazonRef'] = "CASO "+n_atencion+"-" + str(self.sii_batch_number)
            lin_ref = 2
            ref_lines.extend([{'Referencia':ref_line}])
        if self.referencias :
            for ref in self.referencias:
                ref_line = {}
                ref_line = collections.OrderedDict()
                ref_line['NroLinRef'] = lin_ref
                if not self._es_boleta():
                    if  ref.sii_referencia_TpoDocRef:
                        ref_line['TpoDocRef'] = ref.sii_referencia_TpoDocRef.sii_code
                        ref_line['FolioRef'] = ref.origen
                    ref_line['FchRef'] = ref.fecha_documento or datetime.strftime(datetime.now(), '%Y-%m-%d')
                if ref.sii_referencia_CodRef not in ['','none', False]:
                    ref_line['CodRef'] = ref.sii_referencia_CodRef
                ref_line['RazonRef'] = ref.motivo
                if self._es_boleta():
                    ref_line['CodVndor'] = self.seler_id.id
                    ref_lines['CodCaja'] = self.journal_id.point_of_sale_id.name
                ref_lines.extend([{'Referencia':ref_line}])
        dte['item'] = invoice_lines['invoice_lines']

        dte['reflines'] = ref_lines
        dte['TEDd'] = self.get_barcode(invoice_lines['no_product'])
        return dte

    def _dte_to_xml_2(self, dte):
        ted = dte['Documento ID']['TEDd']
        dte['Documento ID']['TEDd'] = ''
        xml = dicttoxml.dicttoxml(
            dte, root=False, attr_type=False) \
            .replace('<item>','').replace('</item>','')\
            .replace('<reflines>','').replace('</reflines>','')\
            .replace('<TEDd>','').replace('</TEDd>','')\
            .replace('</Documento_ID>','\n'+ted+'\n</Documento_ID>')
        return xml

    def _totales_2(self, MntExe=0, no_product=False, taxInclude=False):
        Totales = collections.OrderedDict()
        if self.sii_document_class_id.sii_code == 34 or (self.referencias and self.referencias[0].sii_referencia_TpoDocRef.sii_code == '34'):
            Totales['MntExe'] = int(round(self.amount_total, 0))
            if  no_product:
                Totales['MntExe'] = 0
        elif self.amount_untaxed and self.amount_untaxed != 0:
            if not self._es_boleta() or not taxInclude:
                IVA = False
                for t in self.tax_line_ids:
                    if t.tax_id.sii_code in [14, 15]:
                        IVA = t
                if IVA and IVA.base > 0 :
                    Totales['MntNeto'] = int(round((IVA.base), 0))
            if MntExe > 0:
                Totales['MntExe'] = int(round( MntExe))
            if not self._es_boleta() or not taxInclude:
                if IVA:
                    if not self._es_boleta():
                        Totales['TasaIVA'] = round(IVA.tax_id.amount,2)
                    Totales['IVA'] = int(round(IVA.amount, 0))
                if no_product:
                    Totales['MntNeto'] = 0
                    if not self._es_boleta():
                        Totales['TasaIVA'] = 0
                    Totales['IVA'] = 0
            if IVA and IVA.tax_id.sii_code in [15]:
                Totales['ImptoReten'] = collections.OrderedDict()
                Totales['ImptoReten']['TpoImp'] = IVA.tax_id.sii_code
                Totales['ImptoReten']['TasaImp'] = round(IVA.tax_id.amount,2)
                Totales['ImptoReten']['MontoImp'] = int(round(IVA.amount))
        monto_total = int(round(self.amount_total, 0))
        if no_product:
            monto_total = 0
        Totales['MntTotal'] = monto_total

        #Totales['MontoNF']
        #Totales['TotalPeriodo']
        #Totales['SaldoAnterior']
        #Totales['VlrPagar']
        return Totales
