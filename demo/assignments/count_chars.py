filename = input("Enter the file name:")
upper = lower = digits = others = 0
with open(filename, "rt") as f:
    for ch in f.read():
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            others += 1

print(f"Upper chars = {upper}\nLower chars = {lower}\nDigits = {digits} \nOthers = {others}")
