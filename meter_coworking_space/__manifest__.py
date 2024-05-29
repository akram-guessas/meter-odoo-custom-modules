{
    "name": "Meter CoWorking Space",
    "version": "1.0",
    "depends": [
        "base_setup", "mail", "website_sale", "sale_renting"
    ],
    "data": [
        "security/ir.model.access.csv",

        "data/product_categories.xml",
        "data/meter_space_page.xml",

        "views/sale_order_views.xml",
        "views/meter_all_actions.xml",
        "views/meter_floor_menus.xml",
        "views/meter_floor_views.xml",
        "views/meter_coworking_space_menu.xml",
        "views/product_template_views.xml",

    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
