from inventory import Inventory
from supplier import Supplier
from file_handler import load_products


inventory = Inventory()

supplier = Supplier(
    "S001",
    "Tech Supplies",
    "sales@test.com"
)

# Test 1: Load CSV containing valid and invalid products
print("\nTEST 1: Loading CSV file")

load_products("test_products.csv", inventory, supplier)

print("\nProducts currently in inventory:")
inventory.display_all()


# Test 2: Attempt to load a missing file
print("\nTEST 2: Loading missing CSV file")

load_products("missing_products.csv", inventory, supplier)
