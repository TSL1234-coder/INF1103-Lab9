import unittest

from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "sales@test.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop",
            1200, 10, self.supplier, weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "P002", "Ebook",
            15, 100, self.supplier, download_size=50
        )

        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "unknown", "P003", "Unknown",
                20, 5, self.supplier
            )

    def test_physical_product_without_weight(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P004", "Laptop",
                1200, 10, self.supplier
            )


if __name__ == "__main__":
    unittest.main()
