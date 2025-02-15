# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="MICROSOFT"

    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

p=Programmer("Kshamay",120000,577101)
print(p.company,p.name,p.salary,p.pincode)        