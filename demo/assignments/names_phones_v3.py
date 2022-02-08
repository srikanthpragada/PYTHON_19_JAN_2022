names = ["A", "B", "C", "D", 'E']
phones = ["3939393", "3939393", "93939333"]

if len(names) > len(phones):
    for idx, name in enumerate(names):
        if idx >= len(phones):
            phone = "Unknown"
        else:
            phone = phones[idx]
        print(f"{name:15} {phone}")
else:
    for idx, phone in enumerate(phones):
        if idx >= len(names):
            name = "Unknown"
        else:
            name = names[idx]

        print(f"{name:15} {phone}")
