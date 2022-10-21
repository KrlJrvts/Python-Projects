# # Collections
#
# # List
#  # add, remove or rename values
# colors = ["orange", "black", "white", "pink", "pink"]
# #
# colors.append("yellow")
# print(colors[3])
# #
# #
# colors.remove("pink")
# #
# colors.remove("pink")
# #
# print(colors)
#
# print(len(colors))
#
# .pop()
# .del()

# # elements can be replaced
# nested_colors = [
#     ["white", "black", "grey"],
#     ["red", "orange", "pink"],
#     ["green", "blue", "violet"]
# ]
#
# print(nested_colors[2][0])
#
# # tuples - u can't change elements - it is what it is
# animals = ("cat", "dog", "rat", "horse")
#
# print(len(animals))

# dictionaries - always { & }
#
brands = {
    "Smartphone": "Apple",
    "Computer": "Asus",
    "Headphones": [
        {
            "test1": "value",
            "test2": ["value2", "value4"]
        },
        {
            "test3": "value3",
            "test4": ["value4", "value5"]
        }
    ]
}

print(brands.get("Headphones")[0].get("test2")[1])


# print(brands["Headphones"])
# print(brands.get("Headphones")[1])

# brands_list = ["Apple", "Asus", "Sony"]
# print(brands_list[2])

# set  - Sets are not indexed. unordered, immutable (nothing can be changed), set accepts different values
# Can include all data types
# can be countable

# ikea = {"sofas", "dishes", "candles", "sofas"}
# print(ikea)


# string interpolation
# title = "Mr."
# name = "Kuuba"
# surname = "Tamm"
# age = ", 46"
# hello = "Hello, {} {} {} {}"

# print(hello.format(title, name, surname, age))

# f' string interpolation

# hello_f = f"Hello, {title} {name} {surname}"

# print(hello_f)

# modulo string interpretation

# hello_modulo = "Hello, %s %s %s"
#
# print(hello_modulo % (title, name, surname))
