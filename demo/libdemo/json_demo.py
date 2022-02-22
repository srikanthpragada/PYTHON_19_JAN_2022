import json

class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

p = Person("Jason", "39393933")
print(p.__dict__)
print( json.dumps(p.__dict__))
