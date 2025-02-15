# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a=4

o=demo()
print(o.a)  #Prints the class attribute because instance attributes is not present
o.a=0       #Instance attribyte is set
print(o.a)  #Prints the instance  attribute because instance attributes is  present