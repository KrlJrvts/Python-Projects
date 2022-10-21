from math import sqrt
from time import sleep

# # # definign a function
# # def get_hello_world():
# #     print("Hello World!")
#
#
# # calling the function
# # get_hello_world()
#
# def print_2(text):
#     print(text)
#
#
# print_2("hello world!")


""":first_place_medal:EXTRA (optional): Refactor (remake) your own calculator 
from the homework to incorporate the mathematical operations into the functions you create."""

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)


def root(first_number):
    result = sqrt(first_number)
    print(f"Square root of {first_number} is {format(result, '.2f')}")


def percentage(first_number, second_number):
    if second_number != 0:
        result = (first_number / second_number) * 100
        print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
    else:
        print("You cannot get percentage from 0")


def divide():
    if second_number != 0:
        result = first_number / second_number
        print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
    else:
        print("You cannot divide by 0")


def adding():
    result = first_number + second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def deduction():
    result = first_number - second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def multiple():
    result = first_number * second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def stepping():
    result = first_number ** second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


# __________________________________________________________________________

first_number = input("Write first number: ")
print("Accepted operation symbols: +, -, /, *, %, **, root")
symbol = input("Operation: ")   # + or -

if symbol == "root" and first_number.isnumeric():
    first_number = float(first_number)
    root()

elif symbol == "root" and not first_number.isnumeric():
    print(f"{first_number} isn't numeric value, you cannot calculate Square root.")

else:
    second_number = input("Enter second number: ")

    result = None
    first_number = float(first_number)
    second_number = float(second_number)
    if symbol == "%":
        percentage()
    elif symbol == "/":
        divide()
    elif symbol == "+":
        adding()
    elif symbol == "-":
        deduction()
    elif symbol == "*":
        multiple()
    elif symbol == "**":
        stepping()
    else:
        print("Please insert correct operator.")
