from math import sqrt
from time import sleep

""":first_place_medal:EXTRA (optional): Refactor (remake) your own calculator 
from the homework to incorporate the mathematical operations into the functions you create."""

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)

first_number = True
second_number = None


def root():
    result = sqrt(first_number)
    print(f"Square root of {first_number} is {format(result, '.2f')}")


def percentage():
    if second_number != 0:
        result = (first_number / second_number) * 100
        print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
    else:
        print("You cannot get percentage from 0")


def division():
    if second_number != 0:
        result = first_number / second_number
        print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")
    else:
        print("You cannot divide by 0")


def adding():
    result = first_number + second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def deduct():
    result = first_number - second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def multiple():
    result = first_number * second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


def stepping():
    result = first_number ** second_number
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}.")


# __________________________________________________________________________


while True:
    first_number = input("Write first number: ")
    if first_number.isnumeric() == False:
        print("Please enter numeric value!")
    elif first_number.isnumeric() == True:
        # print("Accepted operation symbols: +, -, /, *, %, **, root")
        # symbol = input("Operation: ")  # + or -
        while True:
            print("Accepted operation symbols: +, -, /, *, %, **, root")
            symbol = input("Operation: ")  # + or -
            if symbol == ("+" or not symbol == "-"
                          or not symbol == "/"
                          or not symbol == "*"
                          or not symbol == "%"
                          or not symbol == "**"
                          or not symbol == "root") == False:
                print("Please enter supported operator")
            elif symbol == "root":
                first_number = float(first_number)
                root()
            else:
                second_number = input("Enter second number: ")
                while False:
                    if not second_number.isnumeric() == True:
                        print("Please enter numeric value")
                    elif second_number.isnumeric() == False:
                        first_number = float(first_number)
                        second_number = float(second_number)
                        if symbol == "%":
                            percentage()
                        elif symbol == "/":
                            division()
                        elif symbol == "+":
                            adding()
                        elif symbol == "-":
                            deduct()
                        elif symbol == "*":
                            multiple()
                        elif symbol == "**":
                            stepping()
                        else:
                            print("Please insert correct operator.")
