class Student:
    def __init__(self, n, g):
        self.name = n
        self.group = g

    def info(self):
        print(f"name : {self.name}\ngroup : {self.group}")
        


class Aspirant (Student):
    def __init__(self, n, g, d):       
        Student.__init__(self, n, g)
        self.defence = d

    def info(self):
        Student.info(self)
        print(f"defence : {self.defence}\n")

a = Student("Tom","2")
b = Aspirant("Kate","3","Math")
a.info()
print()
b.info()
