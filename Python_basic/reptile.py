from animal import Animal


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
