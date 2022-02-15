class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p1 = Player("Ronaldo", 37)
p2 = Player("Dhoni", 40)
p3 = Player("Ronaldo", 37)

print(p1)
print(str(p1))  # p1.__str__()
print(p1 == p3)  # p1.__eq__(p3)
print(p1 != p2)  # p1.__eq__(p2)

#print(p1 > p2)

players = [Player("A", 20), Player("C", 30), Player("B", 28)]

for p in sorted(players):
    print(p)
