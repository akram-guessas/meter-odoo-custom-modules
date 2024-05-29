{
    "name": "Meter Store Space",
    "version": "1.0",
    "depends": [
        "base_setup", "mail", "website_sale", "sale_renting"
    ],
    "data": [
        "security/ir.model.access.csv",
        # "report/reservation_templates.xml",
        # "report/reservation_reports.xml",
        # "report/full_report.xml",
        # "report/full_report_template.xml",
        # "report/smart_office_templates.xml",

        "data/product_categories.xml",
        "data/meter_space_page.xml",

        "views/meter_all_actions.xml",
        "views/meter_floor_menus.xml",
        "views/meter_floor_views.xml",
        "views/meter_coworking_space_menu.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",

        # "views/mtr_booking_views.xml",
        # "views/mtr_booking_menus.xml",
        # "views/mtr_building_menus.xml",
        # "views/mtr_building_views.xml",
        #
        # "views/mtr_office_menus.xml",
        # "views/mtr_office_views.xml",
        # "views/mtr_office_services_menu.xml",
        # "views/mtr_office_services_views.xml",
        # "views/mtr_tags_menu.xml",
        # "views/mtr_tags_views.xml",
        # "views/mtr_space_pricing_menu.xml",
        # "views/mtr_space_pricing_views.xml",
        # "views/mtr_coworking_space_menu.xml",
        #
        # "data/product_categories.xml",
        # "data/mtr_space_page.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
