# Add a static method in problem 2, to greet the user with hello.

Number=int(input("Enter a number:"))

class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of the number is:{self.n*self.n}")
    
    def cube(self):
        print(f"The cube of the number is:{self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The square of the number is:{self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello there!!")

f=Calculator(Number)
f.greet()
f.square()
f.cube()
f.squareroot()
