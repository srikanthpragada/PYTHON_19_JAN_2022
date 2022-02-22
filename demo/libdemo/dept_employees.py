f = open("employees.txt", "rt")
depts = {}

for line in f.readlines():
    dname, ename, salary = line.split(",")
    if dname in depts:
        depts[dname].append((ename, salary.strip()))
    else:
        depts[dname] = [(ename, salary.strip())]

f.close()

for dname, employees in depts.items():
    total = 0
    enames = []
    for e in employees:
        enames.append(e[0])
        total += int(e[1])

    print(f"{dname:10} {total // len(enames):8} {','.join(enames)}  ")


