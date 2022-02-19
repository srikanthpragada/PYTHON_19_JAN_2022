# Generator
def numbers():
    for n in range(1, 5):
        yield n


g = numbers()
print(type(g))
print(next(g))
print(next(g))

# for v in n:
#     print(v)

# Generator Expression
ge = (n for n in range(10, 15))
print(next(ge))
