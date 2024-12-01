'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file "Hi-score.txt" which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''

def game():
    # Simulate the game and return a score as an integer
    import random
    return random.randint(1, 100)

def update_hi_score():
    # Read the current Hi-score from the file
    try:
        with open("Hi-score.txt", "r") as file:
            hi_score = file.read()
            hi_score = int(hi_score) if hi_score.strip().isdigit() else 0
    except FileNotFoundError:
        hi_score = 0  # If file does not exist, consider Hi-score as 0

    # Play the game and get the new score
    new_score = game()
    print(f"Your score: {new_score}")

    # Update the Hi-score if the new score is greater
    if new_score > hi_score:
        print(f"New Hi-score: {new_score}")
        with open("Hi-score.txt", "w") as file:
            file.write(str(new_score))
    else:
        print(f"Current Hi-score remains: {hi_score}")

# Run the program
update_hi_score()

