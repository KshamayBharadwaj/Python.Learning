# Write a class “Calculator” capable of finding square, cube and square root of a number.

Number=int(input("Enter a nuber:"))

class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of the number is:{self.n*self.n}")
    
    def cube(self):
        print(f"The cube of the number is:{self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The square of the number is:{self.n**1/2}")

f=Calculator(Number)
f.square()
f.cube()
f.squareroot()



