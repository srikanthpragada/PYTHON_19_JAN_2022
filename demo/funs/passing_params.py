def fun(v):
    print(id(v))
    v = 0
    print(id(v))


a = 100
print(id(a))
fun(a)
print(a)   # 0 or 100
