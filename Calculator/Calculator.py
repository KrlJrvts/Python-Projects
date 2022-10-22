from time import sleep
from math import sqrt


"""EXTRA (optional): Refactor (remake) your own calculator
from the homework to incorporate the mathematical operations into the functions you create."""

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)


def root():
    return sqrt(first_number)


def percentage():
    return (first_number / second_number) * 100


def divide():
    return first_number / second_number


def add():
    return first_number + second_number


def deduct():
    return first_number - second_number


def multiple():
    return first_number * second_number


def stepping():
    return first_number ** second_number


# __________________________________________________________________________

first_number = input("Write first number: ")
print("Accepted operation symbols: +, -, /, *, %, **, root")
symbol = input("Operation: ")   # + or -

if symbol == "root" and first_number.isnumeric():
    first_number = float(first_number)
    print(f"Root of {first_number} is {root()}.")
elif symbol == "root" and not first_number.isnumeric():
    print(f"{first_number} isn't numeric value, you cannot calculate Square root.")
else:
    second_number = input("Enter second number: ")

    if second_number == "0" and symbol == "%":
        print("You can't take percentage from 0")
    elif second_number == "0" and symbol == "/":
        print("You can't divide with 0")
    elif not second_number.isnumeric():
        print(f"{second_number} is not a numeric value, please enter enter number.")
    else:
        first_number = float(first_number)
        second_number = float(second_number)

        if symbol == "%":
            print(f"{first_number} is {percentage()} % of {second_number}")
        elif symbol == "/":
            print(f"{first_number} {symbol} {second_number} = {divide()}")
        elif symbol == "+":
            print(f"{first_number} {symbol} {second_number} = {add()}")
        elif symbol == "-":
            print(f"{first_number} {symbol} {second_number} = {deduct()}")
        elif symbol == "*":
            print(f"{first_number} {symbol} {second_number} = {multiple()}")
        elif symbol == "**":
            print(f"{first_number} {symbol} {second_number} = {stepping()}")
        else:
            print(f"{symbol} is not recognized operator, please insert correct operator.")
