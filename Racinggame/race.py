"""
Racing part
    1. Generate track based on raceoptions
    2. Second start race based on speed options from raceoptions
    3. Play game till winner is found
    4. Return to main.py
"""
import random
import cars
from time import sleep
import time


def Race(track, speed_car):
    track1 = (track - 1) * ["_"] + ["|"]
    track2 = (track - 1) * ["_"] + ["|"]
    index_car1 = 0
    index_car2 = 0
    # length = int(track)
    asphalt1 = (index_car1 - 1)  # see number peab olema sama mis random
    asphalt2 = (index_car2 - 1)  # see number peab olema sama mis random
    start_time = time.time()

    while index_car1 <= track or index_car2 <= track:
        if index_car1 >= track and index_car2 >= track:
            print("It's a tie!")
            print("Total race time %s seconds" % round((time.time() - start_time), ndigits=4))
            f = open("scoreboard.txt", "a+")
            f.write("It's a tie! Total race time %s seconds\r \n" % round((time.time() - start_time), ndigits=4))
            f.close()
            break
        elif index_car1 == track and index_car2 < track:
            print(f"Car {cars.car1.car_model} won")
            print("Total race time of winner %s seconds" % round((time.time() - start_time), ndigits=4))
            f = open("scoreboard.txt", "a+")
            f.write(f"Car {cars.car1.car_model} won. Winner race time %s seconds\r \n"
                    % round((time.time() - start_time), ndigits=4))
            f.close()
            break
        elif index_car1 < track and index_car2 == track:
            print(f"Car {cars.car2.car_model} won")
            print("Total race time of winner %s seconds" % (time.time() - start_time))
            f = open("scoreboard.txt", "a+")
            f.write(f"Car {cars.car2.car_model} won. Winner race time %s seconds\r \n"
                    % round((time.time() - start_time), ndigits=4))
            f.close()
            break
        else:
            track1.pop(index_car1)
            track1.insert(index_car1, cars.car1.car_model)
            track2.pop(index_car2)
            track2.insert(index_car2, cars.car2.car_model)
            track1.insert(asphalt1, "_")
            track2.insert(asphalt2, "_")
            print(track1)
            print(track2)
            track1.pop(index_car1)
            track2.pop(index_car2)
            sleep(cars.car1.sleep)
            sleep(cars.car2.sleep)

        if speed_car == "Y":
            speed_car1 = random.randrange(1, 3)
            speed_car2 = random.randrange(1, 3)
            index_car1 += speed_car1
            index_car2 += speed_car2
            if index_car1 > track:
                index_car1 = track
            elif index_car2 > track:
                index_car2 = track
            elif index_car1 > track and index_car2 > track:
                index_car1 = track
                index_car2 = track
        elif speed_car == "N":
            speed_car1 = 1
            speed_car2 = 1
            index_car1 += speed_car1
            index_car2 += speed_car2
