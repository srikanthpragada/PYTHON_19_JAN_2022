names = ["A", "B", "C", "D"]
phones = ["3939393", "3939393"]

for idx, name in enumerate(names):
    if idx >= len(phones):
        phone = "Unknown"
    else:
        phone = phones[idx]

    print(f"{name:15} {phone}")
