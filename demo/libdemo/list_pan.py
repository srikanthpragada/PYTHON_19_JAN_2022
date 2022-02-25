import re

with open("customers.txt", "rt") as f:
    contents = f.read()

pans = re.findall(r"[A-Z]{5}\d{4}[A-Z]", contents)

for pan in sorted(pans):
    print(pan)
