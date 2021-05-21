from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_str):
        if value_str == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value_str

    def calculate_comfort(self):
        return sum(deco.comfort for deco in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        try:
            self.fish.remove(fish)
        except:
            pass

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if len(self.fish) > 0:
            fish = " ".join(f.name for f in self.fish)
            result += f"Fish: {fish}\n"
        else:
            result += f"Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result
