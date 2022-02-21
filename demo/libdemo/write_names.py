names = ["Python", "C#", "Java", "JavaScript", "C++"]

with open(r"names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")
