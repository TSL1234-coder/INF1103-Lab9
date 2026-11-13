# ======================================================================
# =================
# Import class
# =================
# ======================================================================


from inventory import Inventory
from product_factory import ProductFactory
from file_handler import save_inventory, load_inventory, INVENTORY_FILE
from product import Product
from supplier import Supplier


# ======================================================================
# =================
# Functions
# =================
# ======================================================================


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than 0.")
                continue

            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def create_default_products() -> list[Product]:

    # Suppliers created first, then shared with several products
    tech_supplier =  Supplier("S001", "Tech Supplies Inc.", "sales@techsupplies.com")
    soft_supplier =  Supplier("S002", "Software Solutions Ltd.", "hello@softwaresolutions.com")


    return [
        ProductFactory.create("physical", "1001", "Keyboard", 30.00, 10, tech_supplier, 0.8),
        ProductFactory.create("physical", "1002", "Mouse", 20.00, 15, tech_supplier, 0.1),
        ProductFactory.create("physical", "1003", "Monitor", 150.00, 5, tech_supplier, 4.5),
        ProductFactory.create("physical", "1004", "Printer", 200.00, 3, tech_supplier, 7.0),
        ProductFactory.create("digital", "1005", "Photo Editor", 59.90, 100, soft_supplier, 250.0),
        ProductFactory.create("digital", "1006", "E-book", 15.00, 100, soft_supplier, 5.0),
    ]

def show_menu():
    print("\n--------Inventory Management System--------")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Product Stock")
    print("4. Search for Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-------------------------------------------")



def find_supplier(inventory: Inventory, supplier_id: str) -> Supplier | None:
    for product in inventory.get_all_products():
        supplier = product.get_supplier()
        if supplier.get_supplier_id() == supplier_id:
            return supplier
    return None


def ask_supplier(inventory: Inventory) -> Supplier:
    supplier_id: str = input("Enter Supplier ID: ")
    existing: Supplier | None = find_supplier(inventory, supplier_id)

    if existing is not None:
        print(f"Using existing supplier: {existing.get_name()}")
        return existing

    name: str = input("Enter Supplier Name: ")
    contact_email: str = input("Enter Supplier Contact Email: ")
    return Supplier(supplier_id, name, contact_email)


def add_product_input(inventory: Inventory) -> None :
    print("\nProduct type:")
    print("1. Physical Product")
    print("2. Digital Product")
    type_choice: str = input("Enter product type (1 or 2): ")

    if type_choice not in ('1', '2'):
        print("Invalid choice. Please enter 1 or 2.")
        return


    product_id: str = input("Enter Product ID: ")
    name: str = input("Enter Product Name: ")
    price: float = get_positive_float("Enter Product Price: ")
    stock: int = int(input("Enter Product Stock: "))
    supplier: Supplier = ask_supplier(inventory)

    
    if type_choice == '1':
        weight: float = get_positive_float("Enter Product Weight (in kg): ")
        new_product = ProductFactory.create("physical", product_id, name, price, stock, supplier, weight)
    else:
        download_size: float = get_positive_float("Enter Product Download Size (in MB): ")
        new_product = ProductFactory.create("digital", product_id, name, price, stock, supplier, download_size)

    if inventory.add_product(new_product):
        print(f"Product {name} added successfully!")
    

def update_product_stock_input(inventory: Inventory) -> None:
    product_id: str = input("Enter Product ID to update stock: ")

    product: Product | None = inventory.find_product(product_id)
    if product is None:
        print(f"Product with ID {product_id} not found.")
        return

    new_stock:int = int(input(f"Enter new stock for {product.get_name()}: "))
    if product.update_stock(new_stock):
        print(f"Stock for {product.get_name()} updated to {new_stock}.")
    else:
        print(f"Failed to update stock for {product.get_name()}. Please check the input value.")


def search_product_input(inventory: Inventory)-> None:
    product_id: str = input("Enter Product ID to search: ")

    product: Product | None = inventory.find_product(product_id)
    if product is None:
        print(f"\nProduct with ID {product_id} not found.")
    else:
        print("\nProduct found:")
        product.display_information()



def save_inventory_ui(inventory: Inventory) -> None:
    result: bool = save_inventory(inventory)

    if result:
        print("\nInventory saved successfully!")
    else:
        print("\nError saving inventory!")



def setup_inventory(inventory: Inventory) -> None:
    result: str = load_inventory(inventory)

    if result == "loaded":
        print("\nInventory loaded successfully!")
    elif result == "not_found":
        print(f"\nInventory file '{INVENTORY_FILE}' not found. Starting with an empty inventory.")

        for product in create_default_products():
            inventory.add_product(product)
        save_inventory(inventory)
        print("\nA new inventory file has been created with default products.")
    else:
        print("\nError loading inventory!")



# ======================================================================
# =================
# Main program
# =================
# ======================================================================

def main() -> None:
    print("=================================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=================================================================")

    # Create an instance of Inventory
    inventory = Inventory() 

    # Load inventory from file if it exists
    setup_inventory(inventory)  

   


    exit_program: bool = False
    while not exit_program:
        show_menu()
        choice: str = input("Enter your choice (1-6): ")


        if choice == '1':
            inventory.display_all()
        elif choice == '2':
            add_product_input(inventory)
        elif choice == '3':
            update_product_stock_input(inventory)
        elif choice == '4':
            search_product_input(inventory)
        elif choice == '5':
            save_inventory_ui(inventory)
        elif choice == '6':
            save_inventory_ui(inventory)
            print("\nThank you for using the Inventory Management System. Goodbye!")
            exit_program = True
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()