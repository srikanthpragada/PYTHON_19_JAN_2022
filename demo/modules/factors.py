import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py  number")
    exit()


num = int(sys.argv[1])  # Command-line arguments

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n)
