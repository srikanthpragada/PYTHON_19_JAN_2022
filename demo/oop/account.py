class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def getbalance(self):
        return self.balance


a1 = Account(1, "Mark", 100000)  # Create an object
a1.deposit(20000)
print(a1.getbalance())

a2 = Account(2, "Scott")