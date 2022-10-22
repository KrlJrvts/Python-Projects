import random


def game(num):
    game_ended = False
    print(f"Guess the computers number from 1 to {num}")
    while not game_ended:
        computers_number = random.randint(1, int(num))
        players_number = input("Guess computer's number: ")

        while True:
            if not players_number.isnumeric():
                print(f"Please choose numeric value between 1 and {num}")
                break
            elif players_number < str(1) or players_number > str(num):
                print(f"Value is not in game range, please choose new value between 1 and {num}.")
                break
            else:
                if int(players_number) == computers_number:
                    print(f"Computer says: {computers_number}, you say: {players_number}")
                    print("You won!")
                    while True:
                        another_round = input("Play another round on same difficulty level? (y/n)")
                        if another_round == "y":  # !!!Not pulling back to game hardness level options!!!
                            game_ended = False
                            break
                        elif another_round == "n":
                            game_ended = True
                            break
                        else:
                            print("Wrong option.")
                    break
                else:
                    print(f"Computer says: {computers_number}, you say: {players_number}")
                    break
