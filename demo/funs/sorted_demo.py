def sign(n):
    return 1 if n >= 0 else 2


nums = [10, 11, 30, 45, -10, -30]

for n in sorted(nums, key=abs):
    print(n)

# for n in sorted(nums, key=sign):
#     print(n)

for n in sorted(nums, key=lambda v: 1 if v >= 0 else 2):
    print(n)
