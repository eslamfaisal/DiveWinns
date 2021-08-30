from odoo import api, models, fields

class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = "product.product"

    vendor_product_name = fields.Char(string="Vendor Product Name", compute="_compute_vendor")
    vendor_product_code = fields.Char(string="Vendor Product Code", compute="_compute_vendor")
    vendor_id = fields.Many2one(comodel_name="res.partner", string="Vendor", compute="_compute_vendor")

    def _compute_vendor(self):
        for product in self:
            supplier_info = self.env["product.supplierinfo"].search([("product_id", "=", product.id)], limit=1)
            if not supplier_info:
                supplier_info = self.env["product.supplierinfo"].search([("product_tmpl_id", "=", product.product_tmpl_id.id)], limit=1)
            if supplier_info:
                product.vendor_id = supplier_info.name.id
                product.vendor_product_code = supplier_info.product_code
                product.vendor_product_name = supplier_info.product_name
            else:
                product.vendor_id = False
                product.vendor_product_code = ""
                product.vendor_product_name = ""