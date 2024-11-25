# Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(F):
    return 5*(F-32)/9

F=int(input("Enter the temperature in F: "))
c=f_to_c(F)
print(f"{round(c,3)}°c")