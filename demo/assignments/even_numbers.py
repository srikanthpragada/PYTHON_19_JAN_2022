# Print all even numbers from the given number to 0
num = 30

if num % 2 != 0:
    num -= 1

for n in range(num, 0, -2):
    print(n)
