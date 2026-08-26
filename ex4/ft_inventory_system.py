import sys


class EmptyInventory(Exception):
    def __init__(self, message: str = "Inventory is empty"):
        super().__init__(message)


def add_inventory(argv: list[str]) -> dict[str, int]:
    inv: dict[str, int] = {}
    for arg in argv[1:]:
        entry = arg.split(':')
        if len(entry) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name = entry[0]
        if item_name in inv:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            item_quantity = int(entry[1])
        except ValueError as ve:
            print(f"Quantity error for '{item_name}': {ve}")
            continue
        inv[item_name] = item_quantity
    return inv

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    try:
        inventory = add_inventory(sys.argv)
        if not inventory:
            raise EmptyInventory()
        keys: list[str] = []
        values = list(inventory.values())
        for item in inventory.keys():
            keys.append(item)
    
        highest_item = keys[0]
        highest_value = values[0]
        lowest_item = keys[0]
        lowest_value = values[0]
    
        print(f"Got inventory: {inventory}")
        print(f"Item list: {keys}")
        print(f"Total quantity of the {len(keys)} items: {sum(values)}")
    
        for item_key, item_value in inventory.items():
            if item_value > highest_value:
                highest_value = item_value
                highest_item = item_key
            elif item_value < lowest_value:
                lowest_value = item_value
                lowest_item = item_key
            percentage: float = round(item_value * 100 / sum(values), 1)
            print(f"Item {item_key} represents {percentage}%")
    
        print(f"Item most abundant: {highest_item} with quantity {highest_value}")
        print(f"Item least abundant: {lowest_item} with quantity {lowest_value}")
    
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
    except EmptyInventory as error:
        print(error)
