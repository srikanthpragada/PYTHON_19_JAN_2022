
total = 0
with open(r"names.txt", "rt") as f:
    lines = f.readlines()
    for line in lines:
        total += len(line)


print(f"Average length = {total//len(lines)}")




