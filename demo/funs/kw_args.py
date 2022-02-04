def details(*args, **kwargs):
    print(args)
    for t in kwargs.items():
        print(t)


details(a=10, b=20)
details(name='abc', age=20)
details(10, 20, a=10)
