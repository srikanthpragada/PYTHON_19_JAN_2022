data = ["1,Mac Pro", "3,iPhone 11",
        "5,Dell XPS", "2,Logitech Mouse"]

products = {}  # empty dict
for entry in data:
    id, name = entry.split(",")
    products[id] = name

for id, name in sorted(products.items()):
    print(f"{id:5} {name}")
