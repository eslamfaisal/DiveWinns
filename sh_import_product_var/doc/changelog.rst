14.0.1 (Date : 5 Oct 2020)
----------------------------
initial release

14.0.2 (13 Oct 2020)
========================
==> IMPORT PRODUCT VARIANT + PRODUCT TEMPLATE CUSTOM FIELDS ALSO.
==> CODE LITTLE BIT CHANGED.

14.0.3 (9 Feb 2021)
========================
==> [ADD] Create new record in dynamic Many2many field if does not exist.
==> [ADD] Create new record in Product Category field if does not exist.


14.0.4 (6 May 2021)
=======================
==> currected below code.
if row[4].strip() == 'Service':
    tmpl_vals.update({'type' : 'service'})                                          
elif row[4].strip() == 'Storable Product':
    tmpl_vals.update({'type' : 'product'})                                                                            
elif row[4].strip() == 'Consumable':
    tmpl_vals.update({'type' : 'consu'})
                                        
                                        