# Write a program which finds out whether a given name is present in a list or not. 
l=["Kshamay","Manoj","Nithin","Likith","Adarsh"]

name=input("Enter your name: ")

if(name in l):
    print("Your name is present in the list")
else:
    print("Your name is not in the list")