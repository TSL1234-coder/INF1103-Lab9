import os
import json
import csv

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier
from product import Product

INVENTORY_FILE = "inventory.json"


def save_inventory(inventory: Inventory) -> bool:
    products_data: list[dict[str, object]] = []
    for product in inventory.get_all_products():

        supplier: Supplier = product.get_supplier()
        product_data: dict[str, object] = {
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
            "supplier": {
                "supplier_id": supplier.get_supplier_id(),
                "name": supplier.get_name(),
                "contact_email": supplier.get_contact_email()
            }
        }

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "physical"
            product_data["weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            product_data["type"] = "digital"
            product_data["download_size"] = product.get_download_size()

        products_data.append(product_data)

    try:
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(products_data, file, indent=4)
        return True

    except(OSError, json.JSONDecodeError) as e:
            return f"Error loading inventory: {e}"
    

# ======================================================================
# ======================================================================
# ======================================================================

def load_inventory(inventory) -> str:
    if not os.path.exists(INVENTORY_FILE):
        return "not_found"

    try:
        with open(INVENTORY_FILE, 'r') as file:
            products_data = json.load(file)


            # One Supplier object per supplier_id, shared by all its products
            suppliers: dict[str, Supplier] = {}

            for item in products_data:

                supplier_data = item["supplier"]
                supplier_id: str = supplier_data["supplier_id"]

                if supplier_id not in suppliers:
                    suppliers[supplier_id] = Supplier(
                        supplier_id,
                        name=supplier_data["name"],
                        contact_email=supplier_data["contact_email"]
                    )
                supplier: Supplier = suppliers[supplier_id]




              
                product_type = item["type"]

                if product_type == "physical":
                    product = ProductFactory.create(
                        product_type="physical",
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        stock=item["stock"],
                        supplier = supplier,
                        weight=item["weight"]
                    )
                elif product_type == "digital":
                    product = ProductFactory.create(
                        product_type="digital",
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        stock=item["stock"],
                        supplier = supplier,
                        download_size=item["download_size"]
                    )
                else:
                    print(f"Unknown product type: {product_type}. Skipping this product.")
                    continue

                inventory.add_product(product)
            return "loaded"

    except(OSError, json.JSONDecodeError) as e:
        return "error"




def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded_count = 0

    try:
        with open(path, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except FileNotFoundError:
        print(f"File not found: {path}")

    else:
        for row in rows:
            try:
                product_type = row["type"].strip().lower()

                product_id = row["product_id"]
                name = row["name"]
                price = float(row["price"])
                stock = int(row["stock"])

                if product_type == "physical":
                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock=stock,
                        supplier=supplier,
                        weight=float(row["weight"])
                    )

                elif product_type == "digital":
                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock=stock,
                        supplier=supplier,
                        download_size=float(row["download_size"])
                    )

                else:
                    raise ValueError(
                        f"Unknown product type: {product_type}"
                    )

                if inventory.add_product(product):
                    loaded_count += 1

            except ValueError as e:
                print(
                    f"Skipping invalid product "
                    f"{row.get('product_id', 'Unknown')}: {e}"
                )

        print(f"Successfully loaded {loaded_count} products.")

    finally:
        print("Load attempt finished.")
