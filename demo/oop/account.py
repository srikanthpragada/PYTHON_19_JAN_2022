class InsufficientAmountError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Insufficient balance of {self.balance} for withdrawl of {self.amount}"

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
        if amount < 1:
            raise ValueError("Invalid Amount!")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientAmountError(self.balance, amount)
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
a2.withdraw(10000)
