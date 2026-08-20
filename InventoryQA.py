from InventoryManagement import InventorySystem


def test_stock_availability():

    inv = InventorySystem()

    inv.add_product("A", "Laptop", 100)

    result = inv.get_stock("A", "Laptop")

    assert result == 100

    print("Stock availability: PASS")


def test_insufficient_inventory():

    inv = InventorySystem()

    inv.add_product("A", "Laptop", 10)

    result, message = inv.remove_product(
        "A", "Laptop", 20
    )

    assert not result

    print("Insufficient inventory: PASS")


def test_warehouse_transfer():

    inv = InventorySystem()

    inv.add_product("A", "Laptop", 100)
    inv.add_product("B", "Laptop", 20)

    result, message = inv.transfer_stock(
        "A", "B", "Laptop", 30
    )

    assert result
    assert inv.get_stock("A", "Laptop") == 70
    assert inv.get_stock("B", "Laptop") == 50

    print("Warehouse transfer: PASS")


def test_reorder_threshold():

    inv = InventorySystem()

    inv.add_product("A", "Mouse", 10)

    result = inv.low_stock(
        "A", "Mouse", 10
    )

    assert result

    inv.reorder("A", "Mouse", 20)

    assert inv.get_stock("A", "Mouse") == 30

    print("Reorder threshold: PASS")


def test_invalid_product():

    inv = InventorySystem()

    result = inv.get_stock(
        "A", "Keyboard"
    )

    assert result == 0

    print("Invalid product: PASS")


def test_negative_inventory():

    inv = InventorySystem()

    result, message = inv.add_product(
        "A", "Laptop", -10
    )

    assert not result

    print("Negative inventory: PASS")


def test_multiple_warehouses():

    inv = InventorySystem()

    inv.add_product("A", "Laptop", 10)
    inv.add_product("B", "Laptop", 50)
    inv.add_product("C", "Laptop", 20)

    warehouse = inv.select_warehouse(
        "Laptop", 40
    )

    assert warehouse == "B"

    print("Multiple warehouses: PASS")


def test_concurrent_orders():

    inv = InventorySystem()

    inv.add_product("A", "Laptop", 100)

    result1, message1 = inv.remove_product(
        "A", "Laptop", 40
    )

    result2, message2 = inv.remove_product(
        "A", "Laptop", 30
    )

    assert result1
    assert result2

    assert inv.get_stock(
        "A", "Laptop"
    ) == 30

    print("Concurrent orders: PASS")


def main():

    print("================================")
    print("INVENTORY QA")
    print("================================")

    test_stock_availability()
    test_insufficient_inventory()
    test_warehouse_transfer()
    test_reorder_threshold()
    test_invalid_product()
    test_negative_inventory()
    test_multiple_warehouses()
    test_concurrent_orders()

    print("================================")
    print("ALL INVENTORY TESTS PASSED")
    print("================================")


if __name__ == "__main__":
    main()
