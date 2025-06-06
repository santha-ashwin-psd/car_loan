import frappe

def set_default_theme(doc, method):
    if not doc.desk_theme:
        doc.desk_theme = "modern"
        doc.save(ignore_permissions=True)
