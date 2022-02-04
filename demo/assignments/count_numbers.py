
numbers = {}

while True:
    num = int(input("Enter a number [0 to stop]"))
    if num == 0:
        break

    if num in numbers:  # if number is found
        numbers[num] = numbers[num] + 1
    else:
        numbers[num] = 1     # First occurrence


for num, count in numbers.items():
    print(f"{num:5} {count:3}")