# # car_loan/overrides/session_boot.py
# import frappe
# from frappe import _

# def boot_session(bootinfo):
#     user = frappe.get_doc("User", frappe.session.user)
#     if not user.desk_theme:
#         user.desk_theme = "modern"
#         user.save(ignore_permissions=True)
#         bootinfo.desk_theme = "modern"


import frappe

def boot_session(bootinfo):
    user = frappe.get_doc("User", frappe.session.user)
    if not user.desk_theme:
        user.desk_theme = "modern"
        user.save(ignore_permissions=True)
        bootinfo.desk_theme = "modern"
