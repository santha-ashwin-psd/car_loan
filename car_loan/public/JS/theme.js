frappe.ui.ThemeSwitcher = class CustomThemeSwitcher extends frappe.ui.ThemeSwitcher {
    constructor() {
        super()
    }

    fetch_themes() {
        return new Promise((resolve) => {
            this.themes = [
                {
					name: "light",
					label: __("Frappe Light"),
					info: __("Light Theme"),
				},
				{
					name: "dark",
					label: __("Timeless Night"),
					info: __("Dark Theme"),
				},
				{
					name: "automatic",
					label: __("Automatic"),
					info: __("Uses system's theme to switch between light and dark mode"),
				},

                {
                    name: "modern",
                    label: __("Car Loan"),
                    info: __("Coustome theme"),
                },
            ];

            resolve(this.themes);
        });
    }
}



frappe.ready(() => {

    alert(123); // test
 
    const homeLink = document.querySelector('.navbar-brand.navbar-home');
 
    if (homeLink) {

        homeLink.textContent = '🏠 Home';

        homeLink.href = '/app';

        homeLink.classList.add('btn', 'btn-primary');

    } else {

        console.warn('Element with class "navbar-brand navbar-home" not found.');

    }

});

 