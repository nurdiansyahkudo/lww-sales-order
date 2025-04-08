from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    no_so = fields.Char(string='Sales Order Number', store=True, required=True)

    def action_print_report(self):
        company = self.env['res.company'].browse(self.env.company.id)
        
        if company.name == 'PT. BINA SERVICE':
            return self.env.ref('lww_sales.action_report_bs_so').report_action(self)
        elif company.name == 'PT. SPARTADUA RIBUJAYA':
            return self.env.ref('lww_sales.action_report_spartadua_so').report_action(self)
        elif company.name == 'PT. PRATAMA DATAMAKSIMA':
            return self.env.ref('lww_sales.action_report_pratama_so').report_action(self)
        elif company.name == 'PT. IMADEA MAGKASAMA':
            return self.env.ref('lww_sales.action_report_imadea_so').report_action(self)
        else:
            return self.env.ref('lww_sales.action_report_limawira_so').report_action(self)

    @api.model_create_multi
    def create(self, vals):
        if 'no_so' in vals and vals['no_so']:
            for record in self:
                existing_record = self.env['sale.order'].search([
                    ('no_so', '=', vals['no_so']),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing_record:
                    raise ValidationError('SO already exist!')
        return super().create(vals)

    def write(self, vals):
        if 'no_so' in vals and vals['no_so']:
            for record in self:
                existing_record = self.env['sale.order'].search([
                    ('no_so', '=', vals['no_so']),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing_record:
                    raise ValidationError('SO already exist!')
        return super().write(vals)
    
    def get_sales_report_name(self):
        return 'Sales Order - %s' % (self.no_so)
