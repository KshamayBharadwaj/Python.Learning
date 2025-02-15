class employee:
    Language="Python" #This is class attribute 
    Salary=5000000

    def getinfo(self):
        print(f"The language is {self.Language} and salary is {self.Salary}")
        
kshamay=employee()
kshamay.Language="JAVA" #This is object attribute
kshamayname="Kshamay"
print(kshamayname,kshamay.Language,kshamay.Salary)

kshamay.getinfo()
employee.getinfo(kshamay)