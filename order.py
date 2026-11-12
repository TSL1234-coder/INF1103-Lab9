
from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    """A customer order made up of OrderLine objects."""

    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy | None = None
    ) -> None:

        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

        if discount is None:
            self.__discount: DiscountStrategy = NoDiscount()
        else:
            self.__discount = discount

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
        """Return (product, quantity, subtotal) tuples."""

        return [
            (line.get_product(), line.get_quantity(), line.calculate_subtotal())
            for line in self.__order_lines
        ]

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        total: float = 0.0

        for line in self.__order_lines:
            total += line.calculate_subtotal()

        return self.__discount.apply(total)
