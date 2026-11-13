from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_COST = 5.00  # Base shipping cost in dollars
    RATE_PER_KG = 2.00  # Rate per kilogram in dollars

    def __init__(self, product_id: str, name:str, price: float, stock: int, supplier: Supplier, weight: float)-> None:
        if weight<=0:
            raise ValueError("Product weight must be greater than 0.")

        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight 

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_COST + (self.RATE_PER_KG * self.__weight)