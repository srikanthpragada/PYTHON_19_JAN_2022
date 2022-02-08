def extractdigits(s):
    st = ""
    for c in s:
        if c.isdigit():
            st += c

    return int(st)

def extractspecial(s):
    st = ""
    for c in s:
        if not (c.isalnum() or c.isspace()):
            st += c

    return st


values = ["ABC123", "AB7878", "383ABC333"]

for n in map(extractdigits, values):
    print(n)

values = ["ABC,23", "AB7-87,8", "383A;BC3;33"]
for n in map(extractspecial, values):
    print(n)
