
# dynamic class
class Animal:
    # functions in class are called methods
    # "init" is shortened of "initialization" or starting the object defined by class
    def __init__(
            self,
            name: str,
            color: str,
            weight: float,
    ):
        self.name = name
        self.color = color
        self.weight = weight


dog = Animal(name="Joy", color="White", weight=35.4)
cat = Animal("Panda", "Black and White", 9.5)
print(dog.name)
print(dog.color)

print(cat.name)
print(cat.weight)


class Reptiles(Animal):
    def __init__(
            self,
            can_breath_underwater: bool,
            has_shell: bool,
            name: str,  # those have to have every time (below)
            color: str,
            weight: float
    ):
        super().__init__(name, color, weight)
        self.can_breath_underwater = can_breath_underwater
        self.has_shell = has_shell


turtle = Reptiles(True, True, "Donatella", "Green", 50.8)
