import frappe
from frappe import _

@frappe.whitelist()
def switch_theme(theme):
    theme = theme.lower()  # Normalize casing
    allowed_themes = ["dark", "light", "automatic", "greenish", "modern"]

    if theme in allowed_themes:
        frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)
        frappe.msgprint(_("Theme switched to {0}").format(theme))
    else:
        frappe.throw(_("Invalid theme: {0}").format(theme))
