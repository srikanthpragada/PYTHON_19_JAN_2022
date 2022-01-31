
lst = []

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    lst.append(num)

for n in lst[::-1]:
    print(n)
