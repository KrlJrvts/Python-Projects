# 1. Assign a number to the variable: glass_of_water

glass_of_water = 2

print("I drank", glass_of_water, "glasses of water today.")


# 2. Fill the print function, so it prints glass_of_water

glass_of_water = 3
glass_of_water += 1

print(glass_of_water)


# 3. Assign an integer to the variable, then print it

men_stepped_on_the_moon = 1961

print(men_stepped_on_the_moon)


# 4. Type a couple of words or a short sentence for your variable, then print it

my_reason_for_coding = "To extend my knowledge base and give myself different options at the work market"

print(my_reason_for_coding)


# 5. Assign a float with 2 decimals to the variable below

# global_mean_sea_level_2018 = 21

# Type your code here

# 5.1. option
# int -> float just number change
global_mean_sea_level_2018 = 21.00

print(global_mean_sea_level_2018)
# print(type(global_mean_sea_level_2018))

# 5.2. option
# Based on rounding value
# global_mean_sea_level_2018 = 21.009231421352344213524143124
# limit_float = round(global_mean_sea_level_2018, 2)

# print(limit_float)
# print(type(limit_float))

# 5.3. option
# Adding a value (short option, also -=, *= and /= work)
# global_mean_sea_level_2018 += 0.21

# 5.4. option
# Data type conversion option
# global_mean_sea_level_2018 = float(21)

# print(global_mean_sea_level_2018)
# print(type(global_mean_sea_level_2018))

# print(global_mean_sea_level_2018)

# 5.5. option
# Using Decimal function - Not showing float, more like class function based on Decimal (

from decimal import Decimal

global_mean_sea_level_2018 = float(21)

value = Decimal(global_mean_sea_level_2018)
result = Decimal(value.quantize(Decimal('.01')))
print(result)

# 5.6. option
# ".2f" - works only with string

# print(format(global_mean_sea_level_2018, ".2f"))

# print(type(global_mean_sea_level_2018))


# 6. Assign True or False to the variable below then print it

staying_alive = True

print(staying_alive)


# 7. Using type() function assign the type of the variable "men_stepped_on_the_moon" to answer_7, then print it

men_stepped_on_the_moon = 1961

# Type your code here.

answer_7 = type(men_stepped_on_the_moon)

print(answer_7)


# 8. "my_grade" variable is a string. Convert it to an integer

my_grade = "10"
answer_8 = int(my_grade)

print(answer_8)
# print(type(answer_8))


# 9. "my_temp" variable is a float. Convert it to an integer.

my_temp = 97.70
answer_9 = int(my_temp)

print(answer_9)


# 10. GWP denotes the total economic activity created by the world population collectively in a year

gross_world_product = 84.84
gwp_str = str(gross_world_product)
answer_10 = "In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."

print(answer_10)
