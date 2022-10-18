import random
from race import Race
from time import sleep

"""
Here you choose race options
    Track length options - random or user preferred
    Car's speed - random or fixed
"""
length = None
speed = None


def Race_options():
    print("Please choose game options")
    print("How long race should be?")
    while True:
        print("Random length - R ")
        print("For preferred length insert a number")
        length_track = input("Answer: ")
        print("Please make new choices")
        print("Please make new choices")
        print("Does speed should be randomized?")
        print("Y - Yes")
        print("N - No")
        speed_car = input("Answer: ")
        if length_track == "R" and (speed_car == "Y" or speed_car == "N"):
            track = int(random.randint(10, 30))
            Race(speed_car=speed_car, track=track)
            break
        elif length_track != "R" and length_track.isnumeric() and (speed_car == "Y" or speed_car == "N"):
            track = int(length_track)
            Race(speed_car=speed_car, track=track)
            break
        # elif type(length_track) != int or speed_car == "Y" or speed_car == "N":
        #     print("Please make new choices")
        else:
            print("Please make new choices")
        sleep(2)
