def ispositive(n) -> bool:
    return n > 0


lst = [10, 20, -10, 34, -50]

for n in filter(ispositive, lst):
    print(n)


def has_digit(s) -> bool:
    # print("s ->", s)
    for c in s:
        if c.isdigit():
            return True

    return False


names = ['Java', 'Java 17', 'JavaScript 2020', 'C#']

for n in filter(has_digit, names):
    print(n)
