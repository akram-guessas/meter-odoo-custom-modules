# Meter Coworking Space (Odoo 19)

Manage coworking floors and spaces in Odoo, and book spaces by the hour from sale orders and the website.

This module works on **Odoo 19 Community**. It does not need any Odoo Enterprise module.

## Features

- **Floors:** name, type, capacity, and the list of spaces on each floor.
- **Spaces:** a product with *Is Coworking Space* selected. Spaces show in the *Coworking Space* category of the shop.
- **Bookings:** on a sale order line, set the booking start and end. Odoo calculates the duration in hours.
- **Overlap check:** Odoo refuses to confirm a booking if the same space is already booked for an overlapping period.
- **Website:** the `/space` page opens the shop on the coworking space category.

## Migration from Odoo 17 to Odoo 19

The 17.0 version of this module depended on `sale_renting`, which is an Odoo Enterprise module. The 19.0 version:

- removes the Enterprise dependency and adds its own booking logic (start, end, duration, overlap check)
- replaces `<tree>` views with `<list>` views (changed in Odoo 18)
- updates the website controller to the Odoo 19 `WebsiteSale` API (the `shop()` method no longer has a `ppg` parameter)
- fixes the space count calculation and removes unused code
- adds automated tests

The 17.0 code stays available in the `17.0` branch.

## Installation

1. Add this repository to your `addons_path`.
2. Install **Meter Coworking Space**. It depends on `website_sale`.

## Tests

```bash
odoo-bin -d <database> -i meter_coworking_space --test-enable \
  --test-tags /meter_coworking_space --stop-after-init
```

Result on Odoo 19.0 Community: 6 tests, 0 failed.

## License

LGPL-3. Author: [Akram Guessas](https://www.linkedin.com/in/akram-guessas-611b0318a/).
