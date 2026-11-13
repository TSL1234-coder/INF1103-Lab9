import unittest

from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


class TestDiscountStrategies(unittest.TestCase):

    def test_no_discount(self):
        discount = NoDiscount()
        self.assertEqual(discount.apply(100), 100)

    def test_percentage_discount(self):
        discount = PercentageDiscount(10)
        self.assertEqual(discount.apply(100), 90)

    def test_bulk_discount_applied(self):
        discount = BulkDiscount(200, 20)
        self.assertEqual(discount.apply(250), 230)

    def test_bulk_discount_not_applied(self):
        discount = BulkDiscount(200, 20)
        self.assertEqual(discount.apply(150), 150)

    def test_student_discount(self):
        discount = StudentDiscount()
        self.assertEqual(discount.apply(250), 225)


if __name__ == "__main__":
    unittest.main()
