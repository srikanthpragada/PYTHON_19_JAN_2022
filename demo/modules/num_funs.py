# Number related functions
PI = 3.14


def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0


# testing - to be executed when module is run as script
if __name__ == '__main__':
    print("Testing...")
    print(iseven(10))
    print(ispositive(-10))