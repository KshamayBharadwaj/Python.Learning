class Employee:
    company="ITC"
    name="Kshamay"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")


class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all language here is your language:{self.language}")


class programmer(Employee,Coder):
    company="ITC Infotech"
    def showLaunguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
    
a=Employee()
b=programmer()

print(a.company,b.company)

b.show()
b.showLaunguage()
b.printLanguage