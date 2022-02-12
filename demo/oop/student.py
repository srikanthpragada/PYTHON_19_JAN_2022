class Student:
    courses = {'java': 5000, 'python': 8000}

    def __init__(self, name, course, feepaid=0):
        # object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def print_details(self):
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print(f"Feepaid : {self.feepaid}")

    def getfeepaid(self):
        return self.feepaid

    def gettotalfee(self):
        return Student.courses[self.course]

    def getdue(self):
        return self.gettotalfee() - self.getfeepaid()


s1 = Student("Jack", "python", 5000)
# s1.feepaid = 10000
s1.print_details()

s2 = Student("Ben", "java", 2000)
s2.payment(2000)
print(s2.getfeepaid())
print(s2.getdue())
