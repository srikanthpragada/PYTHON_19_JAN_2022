names = ["A", "B", ]
phones = ["3939393", "3939393" , "93939333"]

largest = names if len(names) >= len(phones) else phones
smallest = names if len(names) < len(phones) else phones

for idx, v1 in enumerate(largest):
    if idx >= len(smallest):
        v2 = "Unknown"
    else:
        v2 = smallest[idx]

    print(f"{v1} {v2}")
