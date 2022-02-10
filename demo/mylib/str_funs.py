def starts_with_digit(st):
    return st[0].isdigit()

def count_digits(st):
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count

