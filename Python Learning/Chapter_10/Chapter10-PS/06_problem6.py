'''Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. '''

# Answer: Yes, we can change the self-parameter inside a class to something else.

from random import randint

class Train:

    def __init__(slf,trainNo):
        slf.trainNO=trainNo
    
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
