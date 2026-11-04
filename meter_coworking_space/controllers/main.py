from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class CoworkingSpaceController(http.Controller):

    @http.route("/space", type="http", auth="public", website=True, sitemap=False)
    def space(self, **kwargs):
        """Open the shop on the Coworking Space category."""
        category = request.env.ref(
            "meter_coworking_space.coworking_category", raise_if_not_found=False
        )
        return request.redirect(WebsiteSale._get_shop_path(category.sudo() if category else None))
