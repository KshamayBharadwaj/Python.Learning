'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''

mark1=int(input("Enter your first subject marks:"))
mark2=int(input("Enter your second subject marks:"))
mark3=int(input("Enter your third subject marks:"))

# Check for total percentage
total_percentage=(100)*(mark1+mark2+mark3)/300

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You passed your exam",total_percentage)

else:
    print("You are failed,try again next year",total_percentage)