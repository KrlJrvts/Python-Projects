from time import sleep
from math import sqrt


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


