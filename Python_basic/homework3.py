# from Guessing_game.game import game
#
# # 1. Guessing game
#
# """
# 1. Using the base code of the number guessing game, create the following:
#     a. Validation for the players number, so it:
#         i. does not allow to enter any number out of the possible number rage of the computer’s number;
#         ii. does not allow to enter any non-numeric characters;
#         iii. asks you to repeat entering the valid number in range if any of the non-valid characters are entered.
#     b. EXTRA (optional): Create game difficulty levels:
#         i. 1, 3 range is the easy mode;
#         ii. 1, 5 range is the medium mode;
#         iii. 1, 10 range is the hard mode;
#         iv. Allow the user to choose the difficulty before he starts the new round of the game
# """
#
# print("______ Welcome to the guessing game _____")
# game_level = None
# num = None
#
# while True:
#     print("Please choose game difficulty level for Easy - E, Medium - M, Hard - H or to quit game - N")
#     game_level = input("Answer: ")
#     if game_level == "E":
#         game_level = True
#         num = 3
#         game(num=num)
#     elif game_level == "M":
#         game_level = True
#         num = 5
#         game(num=num)
#     elif game_level == "H":
#         game_level = True
#         num = 10
#         game(num=num)
#     elif game_level == "N":
#         game_level = False
#         break
#     else:
#         print("Please insert correct level value.")
#
# print("Thank you for the game!")


# from time import sleep
# from math import sqrt
#
#
#
#
# """:first_place_medal:EXTRA (optional): Refactor (remake) your own calculator
# from the homework to incorporate the mathematical operations into the functions you create."""
#
# print("========================================")
# print("Welcome to the calculator!")
# print("========================================")
# sleep(1)
#
#
# def root():
#     result = sqrt(first_number)
#     print(f"Square root of {first_number} is {format(result, '.2f')}")
#
#
# def percentage():
#     if second_number != 0:
#         result = (first_number / second_number) * 100
#         print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#     else:
#         print("You cannot get percentage from 0")
#
#
# def divide():
#     if second_number != 0:
#         result = first_number / second_number
#         print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#     else:
#         print("You cannot divide by 0")
#
#
# def add():
#     result = first_number + second_number
#     print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#
#
# def deduct():
#     result = first_number - second_number
#     print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#
#
# def multiple():
#     result = first_number * second_number
#     print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#
#
# def stepping():
#     result = first_number ** second_number
#     print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
#
#
# # __________________________________________________________________________
#
# first_number = input("Write first number: ")
# print("Accepted operation symbols: +, -, /, *, %, **, root")
# symbol = input("Operation: ")   # + or -
#
# if symbol == "root" and first_number.isnumeric():
#     first_number = float(first_number)
#     root()
#
# elif symbol == "root" and not first_number.isnumeric():
#     print(f"{first_number} isn't numeric value, you cannot calculate Square root.")
#
# else:
#     second_number = input("Enter second number: ")
#
#     result = None
#     first_number = float(first_number)
#     second_number = float(second_number)
#     if symbol == "%":
#         percentage()
#     elif symbol == "/":
#         divide()
#     elif symbol == "+":
#         add()
#     elif symbol == "-":
#         deduct()
#     elif symbol == "*":
#         multiple()
#     elif symbol == "**":
#         stepping()
#     else:
#         print("Please insert correct operator.")
