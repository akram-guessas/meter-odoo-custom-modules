{
    "name": "Meter Coworking Space",
    "summary": "Manage coworking floors and spaces, and book spaces by the hour "
               "from sale orders and the website.",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "author": "Akram Guessas",
    "website": "https://github.com/akram-guessas/meter-odoo-custom-modules",
    "license": "LGPL-3",
    "depends": ["website_sale"],
    "data": [
        "security/ir.model.access.csv",
        "data/product_categories.xml",
        "data/meter_space_page.xml",
        "views/meter_floor_views.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/meter_all_actions.xml",
        "views/meter_coworking_space_menu.xml",
    ],
    "application": True,
    "installable": True,
}
