with open(r"sortednames.txt", "wt") as f:
    names = []
    while True:
        s = input("Enter a name['end' to stop]:")
        if s == 'end':
            break
        names.append(s)

    for name in sorted(names):
        f.write(name + '\n')
