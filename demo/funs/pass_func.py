def greet(name):
    print("Hello", name)


def goodbye(name):
    print("GoodBye", name)


def message(name, func):
    func(name)


def hello():
    print("Hello")


message("Jack", greet)
message("Mark", goodbye)
message("Bill", hello)
