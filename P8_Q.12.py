inventory={
    "Laptop": 10,
    "Mouse": 25,
    "Keyword": 15
    }
inventory["Monitor"] = 8
inventory["Mouse"] = 30
inventory.pop("Keyword")
print("Final  Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)
