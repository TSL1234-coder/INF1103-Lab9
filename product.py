from abc import ABC, abstractmethod

from supplier import Supplier

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        if price <= 0:
            raise ValueError("Product prices must be greater than 0.")

        if stock < 0:
            raise ValueError("Product stock cannot be negative.")


        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock

        # Association: Product only keeps a reference to Supplier, but does not own it
        self.__supplier: Supplier = supplier


    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock} units")
        print(f"Supplier: {self.__supplier.get_name()}")


    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """To return delivery/fulfillment info for this product"""
        pass