import frappe

@frappe.whitelist(allow_guest=True)
def validate_tracker(self):
        for row in self.comments:
            if "Tracker" in frappe.get_roles(frappe.session.user):
                if frappe.db.exists("Remarks Child", row.name):
                    original_row = frappe.get_doc("Remarks Child", row.name)
                    if row.contact_type != original_row.contact_type:
                        frappe.response["message"] = "You cannot edit existing remarks (Row {0}).".format(row.idx)
                        return frappe.response
                    if row.commends != original_row.commends:
                        frappe.response["message"] = "You cannot edit existing remarks (Row {0}).".format(row.idx)
                        return frappe.response
                    if row.attach != original_row.attach:
                        frappe.response["message"] = "You cannot edit existing remarks (Row {0}).".format(row.idx)
                        return frappe.response
            elif "Admin" in frappe.get_roles(frappe.session.user):
                pass
            else:
                frappe.response["message"] = "You cannot edit existing remarks (Row {0}).".format(row.idx)
                return frappe.response