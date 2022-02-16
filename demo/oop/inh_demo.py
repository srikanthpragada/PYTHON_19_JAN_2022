# Superclass
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(f"Name   : {self.name}")
        print(f"Email  : {self.email}")


# Subclass
class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)
        self.job = job
        self.company = company

    def show(self):
        super().show()
        print(f"Job    : {self.job}")
        print(f"Company: {self.company}")


e = Employee("Scott", "scott@gmail.com", "Programmer", "Google")
e.show()
