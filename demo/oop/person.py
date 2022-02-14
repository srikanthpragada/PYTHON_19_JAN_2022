class Person:
    def __init__(self, name, mobile):
        self.name = name
        # private attribute
        self.__mobile = mobile


p = Person("Jason", "39393933")
print(p.__dict__)
print(p._Person__mobile)