# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f=open("poems.txt")

content=f.read()
if("Twinkle" in content):
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()