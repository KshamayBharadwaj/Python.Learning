class Employee:
    a=1

class Programmer(Employee):
    b=3

class Manager(Programmer):
    c=3

o=Employee()
print(o.a)

p=Programmer()
print(p.a)

q=Manager()
print(q.b)
print(q.a)