def nexteven(n):
    return n + 1 if n % 2 != 0 else n + 2


nums = [10, 11, 30, 45]

for n in map(nexteven, nums):
    print(n)

