
st = input("Enter a string :")
count = 0
for c in st:
    if c.isdigit():
        count += 1

print(count)