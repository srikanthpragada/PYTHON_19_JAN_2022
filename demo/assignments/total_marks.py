data = "56,67,87,54,45"

total = 0
for v in data.split(","):
    total += int(v)

print(total)
