
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine


supplier = Supplier("S001", "Tech Supplies", "sales@test.com")


# Test 1: Invalid product price
try:
    PhysicalProduct("P001", "Laptop", 0, 10, supplier, 2.5)
except ValueError as e:
    print("Price validation:", e)


# Test 2: Invalid product stock
try:
    PhysicalProduct("P002", "Mouse", 20, -5, supplier, 0.5)
except ValueError as e:
    print("Stock validation:", e)


# Test 3: Invalid order quantity
product = PhysicalProduct("P003", "Keyboard", 30, 10, supplier, 0.8)

try:
    OrderLine(product, 0)
except ValueError as e:
    print("Quantity validation:", e)


# Test 4: Invalid physical product weight
try:
    PhysicalProduct("P004", "Monitor", 150, 5, supplier, 0)
except ValueError as e:
    print("Weight validation:", e)


# Test 5: Invalid digital download size
try:
    DigitalProduct("P005", "E-book", 15, 100, supplier, -10)
except ValueError as e:
    print("Download size validation:", e)


# Test 6: Valid product and order line
valid_product = PhysicalProduct(
    "P006", "Laptop", 250, 10, supplier, 2.5
)

valid_order_line = OrderLine(valid_product, 2)

print("Valid order line:", valid_order_line.calculate_subtotal())
