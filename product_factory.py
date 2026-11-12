from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:

    # Allows calling ProductFactory.create() without creating ProductFactory object
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
        weight: float | None = None,
        download_size: float | None = None,
    ) -> Product:

        if product_type.lower() == "physical":
            if weight is None:
                raise ValueError("Physical product requires a weight.")

            return PhysicalProduct(
                product_id, name, price, stock, supplier, weight
            )

        elif product_type.lower() == "digital":
            if download_size is None:
                raise ValueError("Digital product requires a download size.")

            return DigitalProduct(
                product_id, name, price, stock, supplier, download_size
            )

        else:
            raise ValueError("Unknown product type: {product_type}")