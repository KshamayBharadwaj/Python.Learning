import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess the number between 1 and 100 :"))
    if a>n:
        print("Lower number please !!,")    

    else:
        print("Higher number please.")    

print(f"You have guessed the number {n} correct in {guesses} guesses.")
