largest = 0

for i in range(5):
    n = int(input("Enter number :"))
    if n > largest:
        largest = n


print(f"Largest = {largest}")
