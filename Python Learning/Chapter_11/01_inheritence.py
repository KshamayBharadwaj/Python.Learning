class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.sallary}")


class programmer:
    company="ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.sallary}")

    def showLaunguage(self):
        print(f"The name is {self.name} and he is good with {self.launguage} language")

a=Employee()
b=programmer()

print(a.company,b.company)