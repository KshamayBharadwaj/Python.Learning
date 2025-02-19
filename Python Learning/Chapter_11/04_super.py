class Employee:
    def __init__(self):
        print("Constructr of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructr of Programmer")
    b=3

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructr of Manager")
    c=3

o=Employee()
print(o.a)

p=Programmer()
print(p.a)

q=Manager()
print(q.b)
print(q.a)