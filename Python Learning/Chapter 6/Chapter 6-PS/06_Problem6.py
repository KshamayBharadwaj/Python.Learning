'''Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50        
=> F'''

Marks=int(input("Enter your marks"))

if(Marks<=100 and Marks>90):
    grade="Ex"
elif(Marks>80 and Marks<=90):
    grade="A"
elif(Marks>70 and Marks<=80):
    grade="B"
elif(Marks>60 and Marks<=70):
    grade="C"
elif(Marks>50 and Marks<=60):
    grade="D"
elif(Marks<=50):
    grade="F"
else:
    print ("Invalid")

print("Your grade is:",grade)
