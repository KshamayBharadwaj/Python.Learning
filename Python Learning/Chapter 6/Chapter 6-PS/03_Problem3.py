'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. '''

P1="Make a lot of money"
P2="buy now"
P3="subscribe this"
P4="click this"

Message=input("Enter yor comment:")

if((P1 in Message) or (P2 in Message) or(P3 in Message) or(P4 in Message)):
    print("This is spam")
else:
    print("This is not a spam")