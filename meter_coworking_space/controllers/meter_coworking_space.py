from odoo import http
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale

class CoworkingSpaceController(WebsiteSale):

    @http.route([
        '/space',
        '/space/page/<int:page>',
        '/space/category/<model("product.public.category"):category>',
        '/space/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def space(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        # Call the original shop method and cache the response
        if request.env.ref('meter_coworking_space.coworking_category').id:
            category = request.env.ref('meter_coworking_space.coworking_category').id
        return super(CoworkingSpaceController, self).shop(page=page, category=category, search=search, min_price=min_price,
                                                       max_price=max_price, ppg=ppg, **post)