# import os

"""
Scoreboard
Default values
"""


def Scoreboard():

    print("Scoreboard")

    with open("scoreboard.txt", "r") as score:
        for line in score:
            print(line.strip())

    print("Exit scoreboard")
    print("Y -Yes")
    while True:
        exit_score = input("Answer: ")
        if exit_score == "Y":
            break
        else:
            print("Please insert Y to exit scoreboard")
