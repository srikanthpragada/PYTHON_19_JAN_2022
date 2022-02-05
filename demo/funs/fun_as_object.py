def add(a, b):
    return a + b


add2 = add

print(type(add))
print(id(add))

print(add(10, 20))
print(add2(20, 30))
