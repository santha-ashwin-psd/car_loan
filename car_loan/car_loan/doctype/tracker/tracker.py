# Copyright (c) 2025, Manage car loans and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tracker(Document):
	pass




# tracker/tracker/doctype/tracker/tracker.py
# # import frappe
# from frappe.model.document import Document
# import frappe
# from frappe.model.document import Document


# class Tracker(Document):
#     def validate(self):
#         self.check_duplicate_urn()

#     def check_duplicate_urn(self):
#         if self.urn:
#             if frappe.db.exists("Tracker", {"urn": self.urn, "name": ["!=", self.name]}):
#                 frappe.throw(f"URN <b>{self.urn}</b> already exists in another Tracker record.")
