frappe.ready(() => {
    frappe.call('frappe.client.get', {
        doctype: 'User',
        name: frappe.session.user
    }).then(res => {
        const roles = res.message.roles.map(r => r.role.toLowerCase());
        if (!roles.includes("admin")) {
            // Hide the "Users" section from the workspace
            document.querySelectorAll("div.module-card").forEach(card => {
                if (card.innerText.trim().includes("Users")) {
                    card.style.display = "none";
                }
            });
        }
    });
});
