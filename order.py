from order_line import OrderLine
from product import Product

class Order:
    """A customer order made up of OrderLine objects.

    Composition: the Order creates and manages its own OrderLines. Callers
    pass in a Product and a quantity, never an OrderLine.
    """

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id


    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)


    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.__order_lines):
            del self.__order_lines[index]
        else:
            print(f"No order line at position {index}")


    def get_order_lines(self) -> list[tuple[Product, int, float]]:
        """Return (product, quantity, subtotal) tuples.

        The OrderLine objects themselves are not handed out, so a line
        cannot be taken from this Order and moved to another one.
        """

        return [(line.get_product(), line.get_quantity(), line.calculate_subtotal()) for line in self.__order_lines]


    def calculate_total(self) -> float:
        total: float = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()

        return total
