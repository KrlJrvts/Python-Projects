# # # defining a function
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
#
#
# def another_fun():
#     pass
#
#
# another_fun()


# def print_hello_world(name):
#     my_int = 1
#     if my_int == 1:
#         hello = "Hello, world!"
#         return hello  # return exits function body
#     elif my_int != 1:
#         bye = "Bye, World!"
#         return bye
#     else:
#         return  # if you want to get out of function you can always use it
#     print("End of the function")
#
#
#
#
# hello_world = print_hello_world()
#
# print(hello_world)

# def get_greeting(name: str):  # str type.hinting what value it is supported
#     return f"Hi, my name is {name}"
#
#
# print(get_greeting("Kaarel"))

# Scopes - Area of responsibility
# from utility import modify_funny_numbers
# from utility import modify_funny_numbers
# number = 69


# print(modify_funny_numbers(number))

# def get_funny_number():
#  return num


# my_list = ["dog", "playful"]


# def get_dog_sentence():
#     my_sentence = "My {} is really {}".format(*my_list)
#     return my_sentence
#
#
# print(my_sentence)

# Add any number of numbers

# def add(introduction: str, **kwargsargs):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# my_dict = {
#     "k1": "v1",
#     "k2": "v2",
#     "k3": "v3"
# }
#
# print(add("my name is ....", my_dict))  # Prints 15


# # Prints the name and what the user gives
# def print_name_and_something(name, *strings):
#     print(f"First name: {name}")
#     for string in strings:
#         print(string)


# # Add any number of ingredients
# def add_ingredients(**kwargs):
#     result = 0
#     for key in kwargs:
#         result += kwargs[key]
#     return result
#
#
# print(add_ingredients(eggs=3, spam=5, cheese=2))  # Will print 10 key values need also keys (eggs, spam, etc)
#



