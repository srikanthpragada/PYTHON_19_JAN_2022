class Account:
    # class attributes or static variables
    minbal = 10000

    @staticmethod    # Decorator
    def getminbal():
        return Account.minbal

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance

    @property
    def available_balance(self):
        return self.balance - Account.minbal


# print(Account.minbal)  # Class attribute
print(Account.getminbal())    # Static method

a1 = Account(1, "Mark", 100000)  # Create an object
a1.deposit(20000)
print(a1.getbalance())
print(a1.available_balance)   # Property

a2 = Account(2, "Scott")
