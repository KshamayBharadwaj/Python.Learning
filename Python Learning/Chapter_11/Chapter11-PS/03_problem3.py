# Create a class ‘Employee’ and add salary and increment properties to it. 

'''Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary. '''

class Employee():
    salary=500
    incriment=20
    @property
    def salaryafterincriment(self):
        return(self.salary+(self.salary*20)/100)
    
    @salaryafterincriment.setter
    def salaryafterincriment(self,salary):
        return ((salary/self.salary)-1)*100
    
e=Employee()
# print(e.salaryafterincriment)
e.salaryafterincriment=280.8
print(e.incriment) 

