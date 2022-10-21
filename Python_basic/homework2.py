from datetime import date
from datetime import datetime

# 1. String interpolation
"""
Fill in the values with your name, surname and hobbies.

Print out the introduction string using all three types of string interpolations:
    - f-string method
    - .format() method
    - % modulo operator method

Resource: https://www.programiz.com/python-programming/string-interpolation

⭐️ Extra (optional): Using list *unpacking method, make "my_hobbies" as a list,
and upack it using the .format() method with necessary amount of {} placeholders.
"""

# Write your code here
my_name = "Kaarel"
my_surname = "Järveots"
my_birth_country = "Estonia"
my_hobbies = "Guitar, Kitesurfing, Wingfoiling"

# Modify the string according to each interpolation method

# f-string
introduction = f"Hello! My name is {my_name} {my_surname}. I come from {my_birth_country}. " \
               f"My hobbies are {my_hobbies}. Nice to meet you!"

# .format()
introduction_format = "Hello! My name is {} {}. I come from {}. My hobbies are {}. Nice to meet you!"
introduction = (introduction_format.format(my_name,
                                           my_surname,
                                           my_birth_country,
                                           my_hobbies
                                           )
                )

# % modulo
introduction = "Hello! My name is %s %s. I come from %s. My hobbies are %s. Nice to meet you!" \
               % (my_name, my_surname, my_birth_country, my_hobbies)

# Bonus quest
my_hobbies_list = my_hobbies.split()
introduction_format = "Hello! My name is {} {}. I come from {}. My hobbies are {} {} {} . Nice to meet you!"
introduction = (introduction_format.format(my_name,
                                           my_surname,
                                           my_birth_country,
                                           my_hobbies_list[0],
                                           my_hobbies_list[1],
                                           my_hobbies_list[2]
                                           )
                )

# # Don't modify print() function

print(introduction)

# ==================

# 2. List manipulations
"""
You have a list of various meals.

Print out each of the following results using list methods/functions
    - Remove deserts from the meals (first and last one)
    - Add "steak" at the end of the list
    - Replace "spaghetti" with "pasta carbonara"
    - Count the amount of the elements in the list
    - Sort the list in alphabetical order
    
Resource: https://www.w3schools.com/python/python_ref_list.asp

⭐️ Extra (optional): 
    - Merge list "drinks" with the "meals" list (exist various methods, google "python merge lists"),
    demonstrating two ways of doing that.
    
            drinks = ["coke", "coffee", "tea", "milkshake"]
            
"""

# Don't modify this code
meals = ["hot chocolate", "pizza", "spaghetti", "burger", "sushi", "sweet pudding"]

# Write your code here

# Remove deserts
meals.remove("hot chocolate")
meals.remove("sweet pudding")
print(meals)

# Steak
meals.append("steak")
print(meals)

# There is no Spaghetti! Mamma-Mia!!!
meals.remove("spaghetti")
meals.insert(2, "pasta carbonara")
print(meals)

# counting items in the list
print(len(meals))

# abc
print(meals.sort())

# Bonus quest
drinks = ["coke", "coffee", "tea", "milkshake"]

# 1. option - just adding two lists up
menu = meals + drinks
print(menu)

# 2. option - extending existing list
meals.extend(drinks)
print(meals)

# ==================

# 3. Accessing dictionary values
"""
1. Access and print out the following key values (for each value use separate print()):
    - print values of key "electronics"
    - print values of key "adults"
    - print values of key "men's fashion"
    - print values of key "girls' fashion"
    - get "school uniforms" value printed 
    - get "pants" value printed
    
2. Change following values:
    - replace "computers" key values with None (NoneType)
    - remove key "remove me" using one of the dictionary method
    
Resource: https://www.w3schools.com/python/python_ref_dictionary.asp

⭐️ Extra (optional): 
    - print value of key "current date"
    - import the correct Python standard library on the top of the file
    - choose the right module which offers to get the current time
    - replace the "current time" key's value with particular module's method
    
Resource: https://www.programiz.com/python-programming/datetime/current-time
"""

# Don't modify this code
departments = {
    "electronics": ["camera", "GPS", "cell phones", "headphones", "eBook readers"],
    "computers": ["data storage", "monitors", "printers", "scanners", "laptops"],
    "fashion": {
        "adults": [
            {
                "men's fashion": ["shoes", "accessories", "pants", "t-shirts"],
                "women's fashion": ["shoes", "dresses", "jewelry", "handbags"]
            }
        ],
        "kids": [
            {
                "boys' fashion": ["school uniforms", "cartoon shirts"],
                "girls' fashion": ["clothing", "shoes", "watches"]
            }
        ]
    },
    "remove me": 420,
    "extra": {
        "current date": date.today(),
        "current time": "datetime"
    }
}

# Write your code here

# print values of key "electronics"
print(departments.get("electronics"))

# print values of key "adults"
print(departments.get("fashion").get("adults"))

# print values of key "men's fashion"
print(departments.get("fashion").get("adults")[0].get("men's fashion"))

# print values of key "girls' fashion"
print(departments.get("fashion").get("kids")[0].get("girls' fashion"))

# get "school uniforms" value printed
print(departments.get("fashion").get("kids")[0].get("boys' fashion")[0])

# get "pants" value printed
print(departments.get("fashion").get("adults")[0].get("men's fashion")[2])

# replace "computers" key values with None (NoneType)
departments["computers"] = None
print(departments.get("computers"))

# remove key "remove me" using one of the dictionary method
departments.pop("remove me")
print(departments)

# Bonus quest
# print value of key "current date"
print(departments.get("extra").get("current date"))

# import the correct Python standard library on the top of the file - look above
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# replace the "current time" key's value with particular module's method
departments["extra"]["current time"] = str(current_time)
print(departments)


# 4. String manipulations
"""
Do following strings manipulations. Print each result:
    - count all substring in the string
    - find and count all "t" occurrences in the strings
    - capitalize whole string
    - reverse the case of the string

Resource: https://www.w3schools.com/python/python_ref_string.asp
"""

# Don't modify this code
news = "Find the latest breaking news and information on the top stories."

# Write your code here
# count all substring in the string
print(len(news))

# find and count all "t" occurrences in the strings
print(news.count("t"))

# capitalize whole string
print(news.upper())

# reverse the case of the string
print(news[::-1])
