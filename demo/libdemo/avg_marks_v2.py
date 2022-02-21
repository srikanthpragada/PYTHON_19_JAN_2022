
total = 0
with open(r"marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(",")
        name = parts[0]
        total = sum(map(int, parts[1:]))
        print(f"{name:15} {total:4} {total // (len(parts)-1)}")







