with open(r"marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(",")
        if len(parts) < 2:  # ignore line
            continue

        name = parts[0]
        count = 0
        total = 0
        for n in parts[1:]:  # marks from second element onwards
            if n.isdigit():
                total += int(n)
                count += 1

        if count > 0:
          print(f"{name:15} {total:4} {total // count}")
