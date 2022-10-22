import random


class ComputerPlayer:

    def __init__(self, number=0):
        self.number = number

    def set_number(self, level):
        self.number = random.randint(1, level)

    def get_random_generated_number(self):
        return self.number


class RealPlayer:

    def __init__(self, number="0"):
        self.number = number

    def set_my_number(self, number):
        self.number = number

    def get_my_number(self):
        return self.number


def pick_level():
    difficulty = None

    while not difficulty:
        level = input("Please, choose a level - type in 1(easy), 2(medium) or 3(hard): ")
        if level == "1":
            difficulty = 3
        elif level == "2":
            difficulty = 5
        elif level == "3":
            difficulty = 10
        else:
            print("Wrong option!")
    if difficulty:
        choices(int(difficulty))


def choices(level):
    game_won = False

    cpu = ComputerPlayer()
    player1 = RealPlayer()

    # object == a class instance

    while not game_won:
        cpu.set_number(level=level)
        your_number = input(f"Guess the computer's number from 1 to {level}: ")
        player1.set_my_number(your_number)
        if not player1.get_my_number().isnumeric():
            print(f"Please choose a numeric value between 1 and {level}.")
            continue
        elif int(player1.get_my_number()) == cpu.number:
            print(f"Computer says: {cpu.get_random_generated_number()}, you say: {player1.get_my_number()}")
            print("You won!")
            game_won = True
        else:
            print(f"Computer says: {cpu.get_random_generated_number()}, you say: {player1.get_my_number()}")


# From the speed perspective:
# Getters are slower than ".attribute"


pick_level()
