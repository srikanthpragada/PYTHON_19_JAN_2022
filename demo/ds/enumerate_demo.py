l = [10, 20, 30]

idx = 0
for v in l:
    print(idx, v)
    idx += 1

for v in enumerate(l):
    print(v)


for idx, value in enumerate(l, start=1):
    print(idx, value)
