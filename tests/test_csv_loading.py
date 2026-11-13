import unittest
import tempfile
import os
from io import StringIO
from contextlib import redirect_stdout

from inventory import Inventory
from supplier import Supplier
from file_handler import load_products


class TestCSVLoading(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "sales@test.com"
        )

    def test_load_valid_and_invalid_products(self):
        csv_content = (
            "product_id,name,type,price,stock,weight,download_size\n"
            "P001,Laptop,physical,1200,10,2.5,\n"
            "P002,Ebook,digital,15,100,,50\n"
            "P003,Invalid,physical,-10,5,1.0,\n"
        )

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".csv",
            delete=False,
            newline=""
        ) as file:
            file.write(csv_content)
            file_path = file.name

        try:
            output = StringIO()

            with redirect_stdout(output):
                load_products(
                    file_path,
                    self.inventory,
                    self.supplier
                )

            self.assertIn(
                "Successfully loaded 2 products.",
                output.getvalue()
            )
            self.assertIn(
                "Load attempt finished.",
                output.getvalue()
            )
        finally:
            os.remove(file_path)

    def test_missing_csv_file(self):
        output = StringIO()

        with redirect_stdout(output):
            load_products(
                "file_that_does_not_exist.csv",
                self.inventory,
                self.supplier
            )

        self.assertIn("File not found:", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
