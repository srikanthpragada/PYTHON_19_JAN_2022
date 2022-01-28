# Count unique digits
st = input("Enter a string :")
count = 0
seen = ""
for c in st:
    if c.isdigit():
        if c not in seen:   # If not already seen
           count += 1
           seen = seen + c   # Concatenate to string

print(count)