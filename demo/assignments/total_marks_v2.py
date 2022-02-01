data = "56,67,87,abc,45"

total = 0
for v in data.split(","):
    if v.isdigit():
        total += int(v)

print(total)
