# Write a python function which converts inches to cms.
def convert(inch):
    return inch*2.54

n=float(input("Enter a number:"))

print(f"The corresponding value in cms :{convert(n)}")
