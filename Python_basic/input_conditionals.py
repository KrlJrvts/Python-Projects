from time import sleep
from math import sqrt

# 1. Input
"""
Let's create a temperature conversion tool: Celsius to Fahrenheit and vice versa.
    - Find the conversion formula for Celsius and Fahrenheit in the internet
    - Define the formula programmatically
    - Format the float result with 2 decimal points
"""
celsius_1 = float(input("Temperature value in degree Celsius: "))

# Given formula

# find formula for the Celsius conversion to Fahrenheit

fahrenheit_1 = (1.8 * celsius_1) + 32
# Print the result, format floats to 2 decimal points
print(
    f"The {celsius_1} degree Celsius is equal to: {format(fahrenheit_1, '.2f')} Fahrenheit"
)

print("----OR----")

fahrenheit_2 = float(input("Temperature value in degree Fahrenheit: "))

# Find formula for the Fahrenheit conversion to Celsius

celsius_2 = ((fahrenheit_2 - 32) * 5) / 9
# Print the result, format floats to 2 decimal points
print(
    f"The {fahrenheit_2} degree Fahrenheit is equal to: {format(celsius_2, '.2f')} Celsius"
)


# 2. Complete calculator
"""
Add three new operations for the calculator from the class.
    - Add square root operation
    - Add stepping operation
    - Add percentage operation

Fix the textual description of Accepted operation symbols.

⭐️ Extra: Using .isnumeric() and conditional statement, create a validation that prevents the user to enter
the string instead of a number. You are allowed to change the code accordingly.

Resource: https://www.w3schools.com/python/ref_string_isnumeric.asp 
"""

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)

first_number = input("Write first number: ")
print("Accepted operation symbols: +, -, /, *, %, **, root")
symbol = input("Operation: ")   # + or -
if symbol == "root" and first_number.isnumeric():
    first_number = float(first_number)
    result = sqrt(first_number)
    print(f"Square root of {first_number} is {format(result, '.2f')}")

elif symbol == "root" and not first_number.isnumeric():
    print(f"{first_number} isn't numeric value, you cannot calculate Square root.")

else:
    second_number = input("Enter second number: ")
    result = None

    if first_number.isnumeric() and second_number.isnumeric():
        first_number = float(first_number)
        second_number = float(second_number)

        if symbol == "+":
            result = first_number + second_number
        elif symbol == "-":
            result = first_number - second_number
        elif symbol == "*":
            result = first_number * second_number
        elif symbol == "%":

            if second_number != 0:
                result = (first_number / second_number)*100
            else:
                print("You cannot get percentage from 0")
        elif symbol == "**":
            result = first_number ** second_number
        elif symbol == "/":

            if second_number != 0:
                result = first_number / second_number
            else:
                print("You cannot divide by 0")

        if (isinstance(result, int) or isinstance(result, float)) and symbol == "%":
            print(f"Result: {first_number} is {format(result, '.2f')} {symbol} of {second_number}.")
        elif isinstance(result, int) or isinstance(result, float):
            print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
        else:
            print("wrong operation")
    else:
        print("Please enter numeric values instead.")

# 3. Dictionaries and conditionals
"""
You got two dictionaries with the car details.
Depending on the six print() statements, write corresponding
conditional statements, inserting the corresponding print statement
from below. 

Example:

    if neighbours_car.get("price") > my_car.get("price"):
        print("Neighbours car is more expensive than mine")
"""

# Don't change the dictionaries
my_car = {
    "make": "Volkswagen",
    "model": "Golf  4",
    "color": "blue",
    "engine capacity": 1.9,
    "manufacture year": 2000,
    "door count": 5,
    "price": 2300
}

neighbours_car = {
    "make": "BMW",
    "model": "320d",
    "color": "blue",
    "engine capacity": 2.0,
    "manufacture year": 2000,
    "door count": 4,
    "price": 3200
}

# Write your code here
if neighbours_car.get("make") != my_car.get("make"):
    print("Me and my neighbour car makes are not the same")
else:
    print("Me and my neighbour car makes are the same")

if neighbours_car.get("model") != my_car.get("model"):
    print("Me and my neighbour car model are not the same")
else:
    print("Me and my neighbour car model are the same")

if neighbours_car.get("color") != my_car.get("color"):
    print("Our car color is not the same")
else:
    print("Our car color is the same")

if neighbours_car.get("engine capacity") > my_car.get("engine capacity"):
    print("My car engine capacity is smaller than the neighbour's")
elif neighbours_car.get("engine capacity") < my_car.get("engine capacity"):
    print("My car engine capacity is bigger than the neighbour's")
else:
    print("Our car color is the same")

if neighbours_car.get("manufacture year") > my_car.get("manufacture year"):
    print("My car manufacture date is the earlier")
elif neighbours_car.get("manufacture year") < my_car.get("manufacture year"):
    print("My car manufacture date is the later")
else:
    print("Our car manufacture date is the same")

if neighbours_car.get("door count") > my_car.get("door count"):
    print("My car got less doors than the neighbour's")
elif neighbours_car.get("door count") < my_car.get("door count"):
    print("My car got more doors than the neighbour's")
else:
    print("My car got same number of doors than the neighbour's")
