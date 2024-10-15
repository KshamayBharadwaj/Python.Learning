# Write a program to find out whether a given post is talking about “Kshamay” or not.
post=input("Enter your post")

if("Kshamay".lower() in post.lower()):
    print("This post is talking about Kshamay")
else:
    print("This post is not talking about Kshamay")
