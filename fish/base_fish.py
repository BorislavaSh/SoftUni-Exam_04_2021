from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_str):
        if value_str == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value_str

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value_str):
        if value_str == "":
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value_str

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += 5