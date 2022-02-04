def wish(*names):
    for n in names:
        print('Hello', n)


def greet(*names, message = "Hello"):
    for n in names:
        print(message, n)


wish("Roberts", "Andy", "Joe")
wish("Bill")

greet("James", "Van", message = "Good Morning")
greet("James", "Anders")