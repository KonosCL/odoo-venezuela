# -*- coding: utf-8 -*-
#############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    vendor_invoice_number = fields.Char(string='Nro factura proveedor', readonly=True,
        states={'draft': [('readonly', False)]},
        help="El número de factura generado por el proveedor" )
    control_invoice_number = fields.Char(string='Nro de Control', readonly=True,
    	states={'draft': [('readonly', False)]},
    	help='Nro de control de la factura de proveedor')
