
# animal that lives with you: dog, cat etc.
# static class , when each of the values are already predefined

class Pet:
    type_of_animal: str = "cat"  # Attribute of the class
    name: str = "Panda"
    color: str = "black and white"
    age: int = 9


my_first_cat = Pet()
print(f" {my_first_cat.name} is {my_first_cat.age} years old")




