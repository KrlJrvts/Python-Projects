# First program I wrote as a programmer. Date 20220925 at 10:23 (GMT +3)

# Print function
# prints results in the terminal

# Variables - "muutujad"

# Integerid
my_first_number = 400    # snake case style, PEP8 standard
mySecondNumber = 420     # !!!JavaScript style, camel case style, never in Python!!!
my_second_number = 20

a_secret_type_variable = 96

# Strings
my_first_string = "Hello, this is a test!"
my_second_string = "This is a friendly reminder"

# Boolean databases
my_first_bool: bool = True
my_second_bool = False

# Floating numbers ehk numbrid lubatud ka pärast koma kohta
my_first_float = 3.14

# NoneType - in case you do not know anything
my_variable = None

# Prints results to terminal
print("Hello, world!")

print(5 + 5 * 2 - 5 / 2)

print(my_first_number + my_second_number)

print(my_first_string + " " + my_second_string)

print(my_second_string + ": " + str(my_first_number + my_second_number))

# Second part
print(my_variable)

my_variable = "I decided that this will be a string!"

print(my_variable)

# You can redeclare variables all the time
print(my_first_float)

my_first_float = 69.420
print(my_first_float)


# Secret type of function
print(type(a_secret_type_variable))

secret_type = type(a_secret_type_variable)
print(secret_type)
