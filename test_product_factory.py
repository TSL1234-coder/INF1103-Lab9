
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


supplier = Supplier(
    "S001",
    "Tech Supplies",
    "sales@test.com"
)

# Test 1: Create physical product
physical = ProductFactory.create(
    "physical",
    "P001",
    "Laptop",
    250.00,
    10,
    supplier,
    weight=2.5
)

print("Physical product:", isinstance(physical, PhysicalProduct))
print("Is a Product:", isinstance(physical, Product))


# Test 2: Create digital product
digital = ProductFactory.create(
    "digital",
    "P002",
    "E-book",
    15.00,
    100,
    supplier,
    download_size=50.0
)

print("Digital product:", isinstance(digital, DigitalProduct))
print("Is a Product:", isinstance(digital, Product))


# Test 3: Unknown product type
try:
    ProductFactory.create(
        "unknown",
        "P003",
        "Test",
        10.00,
        5,
        supplier
    )
except ValueError as e:
    print("Unknown type:", e)


# Test 4: Missing physical product weight
try:
    ProductFactory.create(
        "physical",
        "P004",
        "Keyboard",
        30.00,
        10,
        supplier
    )
except ValueError as e:
    print("Missing weight:", e)
