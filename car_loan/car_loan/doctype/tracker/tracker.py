# Copyright (c) 2025, Manage car loans and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tracker(Document):
    pass
    # def validate(self):
    #     for row in self.comments:
    #         if "Tracker" in frappe.get_roles(frappe.session.user):
    #             if frappe.db.exists("Remarks Child", row.name):
    #                 original_row = frappe.get_doc("Remarks Child", row.name)
    #                 if row.contact_type != original_row.contact_type:
    #                     frappe.throw(("You cannot edit existing remarks (Row {0}).").format(row.idx))
    #                 if row.commends != original_row.commends:
    #                     frappe.throw(("You cannot edit existing remarks (Row {0}).").format(row.idx))
    #                 if row.attach != original_row.attach:
    #                     frappe.throw(("You cannot edit existing remarks (Row {0}).").format(row.idx))
    #         elif "Admin" in frappe.get_roles(frappe.session.user):
    #             pass
    #         else:
    #             frappe.throw(("You do not have permission to edit or add (Row {0}).").format(row.idx))


