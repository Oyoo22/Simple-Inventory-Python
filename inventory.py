class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def update_item(self, name, quantity):
        if name in self.items:
            self.items[name] = quantity
        else:
            print(f"Item '{name}' not found in inventory.")

    def get_item(self, name):
        if name in self.items:
            return f"{name}: {self.items[name]}"
        else:
            return f"Item '{name}' not found in inventory."

    def total_quantity(self):
        return sum(self.items.values())

    def display_inventory(self):
        for name, quantity in self.items.items():
            print(f"{name}: {quantity}")

# Examples
inventory = Inventory()

# Add items
inventory.add_item("Apples", 10)
inventory.add_item("Bananas", 20)
inventory.add_item("Oranges", 15)

# Updates item quantity.
inventory.update_item("Bananas", 25)

# Retrieving item info.
print(inventory.get_item("Apples"))
print(inventory.get_item("Bananas"))
print(inventory.get_item("Grapes"))  # Item not in inventory

# Displaying total quantity.
print(f"Total quantity of all items: {inventory.total_quantity()}")

# Displaying all items in inventory
inventory.display_inventory()
