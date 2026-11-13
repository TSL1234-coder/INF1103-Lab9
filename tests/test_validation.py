import unittest

from product_factory import ProductFactory
from order_line import OrderLine
from supplier import Supplier


class TestDataValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "sales@test.com"
        )

    def test_invalid_product_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Laptop",
                0, 10, self.supplier, weight=2.5
            )

    def test_invalid_product_stock(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Laptop",
                1200, -1, self.supplier, weight=2.5
            )

    def test_invalid_physical_product_weight(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P003", "Laptop",
                1200, 10, self.supplier, weight=0
            )

    def test_invalid_digital_product_size(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "P004", "Ebook",
                15, 100, self.supplier, download_size=0
            )

    def test_invalid_order_quantity(self):
        product = ProductFactory.create(
            "physical", "P005", "Laptop",
            1200, 10, self.supplier, weight=2.5
        )

        with self.assertRaises(ValueError):
            OrderLine(product, 0)


if __name__ == "__main__":
    unittest.main()
