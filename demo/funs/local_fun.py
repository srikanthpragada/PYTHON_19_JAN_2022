x = 1000   # Global variable

# Enclosing or outer function
def fun1():
    global x
    x = 500
    a = 100    # Enclosing variable
    print('fun1')

    # Local function
    def fun2():
        nonlocal a
        a = 10
        b = 200   # Local variable
        print('fun2', a, b)

    fun2()
    print(a)


fun1()
