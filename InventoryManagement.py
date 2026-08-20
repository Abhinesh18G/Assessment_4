class InventorySystem:

    def __init__(self):
        self.warehouses = {}
        self.suppliers = {}

    def add_product(self, warehouse, product, quantity):
        if quantity < 0:
            return False, "Quantity cannot be negative"

        if warehouse not in self.warehouses:
            self.warehouses[warehouse] = {}

        self.warehouses[warehouse][product] = \
            self.warehouses[warehouse].get(product, 0) + quantity

        return True, "Product added successfully"

    def add_supplier(self, supplier_id, supplier_name):
        self.suppliers[supplier_id] = supplier_name
        return True

    def get_stock(self, warehouse, product):
        if warehouse not in self.warehouses:
            return 0

        return self.warehouses[warehouse].get(product, 0)

    def remove_product(self, warehouse, product, quantity):
        if quantity < 0:
            return False, "Quantity cannot be negative"

        stock = self.get_stock(warehouse, product)

        if stock < quantity:
            return False, "Insufficient inventory"

        self.warehouses[warehouse][product] -= quantity

        return True, "Product removed successfully"

    def transfer_stock(self, source, destination, product, quantity):
        result, message = self.remove_product(
            source, product, quantity
        )

        if not result:
            return False, message

        self.add_product(destination, product, quantity)

        return True, "Stock transferred successfully"

    def low_stock(self, warehouse, product, threshold):
        stock = self.get_stock(warehouse, product)
        return stock <= threshold

    def select_warehouse(self, product, quantity):
        best = None
        highest_stock = -1

        for warehouse in self.warehouses:
            stock = self.get_stock(warehouse, product)

            if stock >= quantity and stock > highest_stock:
                highest_stock = stock
                best = warehouse

        return best

    def reorder(self, warehouse, product, quantity):
        return self.add_product(
            warehouse, product, quantity
        )


def main():

    print("===== INVENTORY MANAGEMENT =====")

    inventory = InventorySystem()

    inventory.add_product("A", "Laptop", 100)
    inventory.add_product("B", "Laptop", 50)
    inventory.add_product("C", "Laptop", 20)

    inventory.add_product("A", "Mouse", 10)

    inventory.add_supplier("S1", "ABC Supplier")

    print("Warehouse A Laptop:",
          inventory.get_stock("A", "Laptop"))

    print("Warehouse B Laptop:",
          inventory.get_stock("B", "Laptop"))

    inventory.transfer_stock(
        "A", "C", "Laptop", 20
    )

    print("After transfer:")

    print("Warehouse A:",
          inventory.get_stock("A", "Laptop"))

    print("Warehouse C:",
          inventory.get_stock("C", "Laptop"))

    warehouse = inventory.select_warehouse(
        "Laptop", 60
    )

    print("Warehouse selected for order:",
          warehouse)

    if inventory.low_stock("A", "Mouse", 10):
        print("Low stock detected for Mouse")

    inventory.reorder("A", "Mouse", 20)

    print("Mouse after reorder:",
          inventory.get_stock("A", "Mouse"))


if __name__ == "__main__":
    main()
