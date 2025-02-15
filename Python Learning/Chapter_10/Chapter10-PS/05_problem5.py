'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.'''

from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNO=trainNo
    
    def bookTicket(self):
        print("Ticket Booked Successfully!!")   

    def getStatus(self):
        print(f"The number of seats available are:{randint(0,100)}")    

    def getFare(self):        
        print(f"The fare for the ticket is:{randint(100,1000)}")

trainNo=int(input("Enter the train number:"))   
t=Train(trainNo)
t.bookTicket()
t.getStatus()
t.getFare()
