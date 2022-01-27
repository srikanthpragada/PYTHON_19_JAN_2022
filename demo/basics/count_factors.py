# Count no. of factors

num = int(input("Enter number : "))

count = 0
for n in range(2, num//2 + 1):
    if num % n == 0:
        count += 1

print(f"Number of factors = {count}")