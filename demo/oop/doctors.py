from abc import ABC, abstractmethod


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print(f"Name       : {self.name}")
        print(f"Department : {self.dept}")

    @abstractmethod
    def get_salary(self):
        pass


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge_per_visit):
        super().__init__(name, dept)
        self.visits = visits
        self.charge_per_visit = charge_per_visit

    def show(self):
        super().show()
        print(f"No. of visit     : {self.visits}")
        print(f"Charge per visit : {self.charge_per_visit}")

    def get_salary(self):
        return self.visits * self.charge_per_visit


class Resident(Doctor):
    def __init__(self, name, dpt, salary):
        super().__init__(name, dpt)
        self.salary = salary

    def show(self):
        super().show()
        print(f"Salary : {self.salary}")

    def get_salary(self):
        return self.salary


r = Resident("Dr. James", "Neurologist", 300000)
c = Consultant("Dr. Kim", "Cardio", 3, 1500)
r.show()
print(r.get_salary())
c.show()
print(c.get_salary())
