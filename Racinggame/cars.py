"""
Input about car "models", some random power and sleep between steps
"""


class Car:

    def __init__(
            self,
            car_model: str,
            power: int,
            sleep: float):
        self.car_model = car_model
        self.power = power
        self.sleep = sleep


car1 = Car("X", 100, 0.3)
car2 = Car("O", 150, 0.3)
