from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import (NoDiscount, PercentageDiscount, BulkDiscount )

supplier =  Supplier("S001", "Tech Supplies", "sales@test.com")

laptop = PhysicalProduct("P001", "Laptop", 250.00, 15, supplier, 2.5)

# Test 1: No discount (default)
order = Order("O001")
order.add_order_line(laptop, 1)

print("No Discount: ", order.calculate_total())

# Test 2: Bulk discount
order.set_discount(BulkDiscount(200,20))

print("Bulk Discount: ", order.calculate_total())


# Test 3: Percentage Discount
order.set_discount(PercentageDiscount(10))

print("Percentage Discount: ", order.calculate_total())


# Test 4: Change back to default
order.set_discount(NoDiscount())

print("Back to no discount: ", order.calculate_total())