class Queue:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data[0]
        del self.data[0]
        return value

    def isEmpty(self):
        return len(self.data) == 0

    def length(self):
        return len(self.data)


q = Queue()
q.add(10)
q.add(20)
q.add(13)
print(q.remove())
print(q.isEmpty())
print(q.length())
