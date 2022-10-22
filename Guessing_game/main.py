from Guessing_game.game import game


"""
1. Using the base code of the number guessing game, create the following:
    a. Validation for the players number, so it:
        i. does not allow to enter any number out of the possible number rage of the computer’s number;
        ii. does not allow to enter any non-numeric characters;
        iii. asks you to repeat entering the valid number in range if any of the non-valid characters are entered.
    b. EXTRA (optional): Create game difficulty levels:
        i. 1, 3 range is the easy mode;
        ii. 1, 5 range is the medium mode;
        iii. 1, 10 range is the hard mode;
        iv. Allow the user to choose the difficulty before he starts the new round of the game
"""

print("______ Welcome to the guessing game _____")
game_level = None
num = None

while True:
    print("Please choose game difficulty level for Easy - E, Medium - M, Hard - H or to quit game - N")
    game_level = input("Answer: ")
    if game_level == "E":
        game_level = True
        num = 3
        game(num=num)
    elif game_level == "M":
        game_level = True
        num = 5
        game(num=num)
    elif game_level == "H":
        game_level = True
        num = 10
        game(num=num)
    elif game_level == "N":
        game_level = False
        break
    else:
        print("Please insert correct level value.")

print("Thank you for the game!")
