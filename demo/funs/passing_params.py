# Immutable - Formal parameter cannot change actual parameter
def fun(v):
    print(id(v))
    v = 0
    print(id(v))


a = 100
print(id(a))
fun(a)
print(a)  # 0 or 100


# Mutable - Formal parameter can change actual parameter
def prepend(lst, value):
    lst.insert(0, value)


l = [1, 2]
prepend(l, 10)
print(l)
