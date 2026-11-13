from product import Product

class OrderLine:
    """One product and a quantity inside an Order.

    Composition: an OrderLine is created and managed by its Order only.
    It refers to a Product but does not own it.
    """

    def __init__(self, product: Product, quantity: int) -> None:

        if quantity <=0:
            raise ValueError("Order quantity must be greater than 0.")

        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity