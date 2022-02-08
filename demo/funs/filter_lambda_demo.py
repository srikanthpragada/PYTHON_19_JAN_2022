lst = [10, 20, -10, 34, -50]

for n in filter(lambda n: n >= 0, lst):
    print(n)

for n in filter(lambda n: n % 10 == 0, lst):
    print(n)