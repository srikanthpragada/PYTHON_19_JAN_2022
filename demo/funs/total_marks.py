data = "56,67,87,54,,45"

onlynumbers = filter(str.isdigit, data.split(","))
total = sum(map(int, onlynumbers))
print(total)
