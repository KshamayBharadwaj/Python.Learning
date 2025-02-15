class employee:
    Language="Python" #This is class attribute 
    Salary=5000000

    def __init__(self,name,Salary,Language):    #dunder method which is automatically called
        self.name=name
        self.Salary=Salary
        self.Language=Language

        print("I am changing the world!")
    
    def getinfo(self):
        print(f"The language is {self.Language} and salary is {self.Salary}")

    @staticmethod
    def greet():
        print("Good Morning")

kshamay=employee("Kshamay",6000000,"JAVA")
# kshamay.name="Kshamay"
print(kshamay.name,kshamay.Language,kshamay.Salary)