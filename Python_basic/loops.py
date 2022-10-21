import random
# animals = ["dog", "cat", "john", "mouse", "snake", "tiger"]
#
# # for loop
# # iterations - one element from list - what you want from where
# for animal in animals:
#     print(animal)
#     if animal == "mouse":
#         break
#
# # continue allows
# for animal in animals:
#     if animal == "john":
#         continue
#     print(animal)


# marbles_in_a_jar = ["red", "red", "red", "blue", "red", "red"]
#
# for marble in marbles_in_a_jar:
#     if marble != "red":
#         break
#     print(marble)


# # string
# for substring in "students":
#     print(substring)
#
# # Dictionary FOR  if we want to print both key and value we have to add .items()
#
# zoo = {
#     "feline": "tiger",
#     "canine": "wolf",
# }
#
# for k, v in zoo.items():
#     print(f"{k} and {v}")

# # vahemiku printimiseks kasuta range ()
# my_range = range(0, 101, 33)
#
# for number in my_range:
#     print(number)

# random_int = random.randint(0, 9)
# print(random_int)

# while loop - loop until get solution

# do not run this code

game_ended = False
another_round = None

print("Guess the computers number from 1 to 3")
while not game_ended:
    # players_number = int(input("You say: "))
    computers_number = random.randint(1, 3)
    players_number = input("Guess computer's number: ")
    # print(f"Computer says: {computers_number}")

    if int(players_number) == computers_number:
        print(f"Computer says: {computers_number}, you say :{players_number}")
        print("You won!")

        while True:  # another_round != "y" or another_round != "n":
            another_round = input("Play another round? (y/n) ")
            if another_round == "y":
                game_ended = False
                break
            elif another_round == "n":
                game_ended = True
                break
            else:
                print("Wrong option.")
    else:
        print(f"Computer says: {computers_number}, you say :{players_number}")
        print("Try again!")

print("Thank you for the game!")
