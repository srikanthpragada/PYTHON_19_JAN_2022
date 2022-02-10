# Number related functions
PI = 3.14


def iseven(n):
    """
    Returns true if the given number is even otherwise false
    :param n:  number to check
    :return:  True/False
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


# testing - to be executed when module is run as script
if __name__ == '__main__':
    print("Testing...")
    print(iseven(10))
    print(ispositive(-10))