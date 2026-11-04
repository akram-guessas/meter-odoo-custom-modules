from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestSpaceBooking(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Test Customer"})
        cls.floor = cls.env["mtr_coworking.floor"].create({"name": "Floor 1", "floor_capacity": 20})
        cls.space = cls.env["product.product"].create({
            "name": "Meeting Room A",
            "type": "service",
            "space_ok": True,
            "floor_id": cls.floor.id,
            "list_price": 15.0,
        })

    def _order(self, start, end):
        return self.env["sale.order"].create({
            "partner_id": self.partner.id,
            "order_line": [(0, 0, {
                "product_id": self.space.id,
                "space_start": start,
                "space_end": end,
            })],
        })

    def test_duration_and_flags(self):
        order = self._order("2026-11-10 09:00:00", "2026-11-10 12:00:00")
        self.assertEqual(order.order_line.space_duration, 3.0)
        self.assertTrue(order.order_line.is_space)
        self.assertTrue(order.is_space_order)

    def test_floor_counts_spaces(self):
        self.assertEqual(self.floor.num_spaces, 1)

    def test_end_before_start_is_refused(self):
        with self.assertRaises(ValidationError):
            self._order("2026-11-10 12:00:00", "2026-11-10 09:00:00")

    def test_missing_dates_block_confirmation(self):
        order = self._order(False, False)
        with self.assertRaises(UserError):
            order.action_confirm()

    def test_overlapping_booking_is_blocked(self):
        self._order("2026-11-10 09:00:00", "2026-11-10 12:00:00").action_confirm()
        second = self._order("2026-11-10 11:00:00", "2026-11-10 13:00:00")
        with self.assertRaises(ValidationError):
            second.action_confirm()

    def test_next_booking_is_accepted(self):
        self._order("2026-11-10 09:00:00", "2026-11-10 12:00:00").action_confirm()
        second = self._order("2026-11-10 12:00:00", "2026-11-10 14:00:00")
        second.action_confirm()
        self.assertEqual(second.state, "sale")
