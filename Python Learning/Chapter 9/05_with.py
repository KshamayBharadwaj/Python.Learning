F=open("file.txt")
data=F.read()
print(data)
F.close()

# The same can be written using with statement like this
with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file