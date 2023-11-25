from abc import ABC, abstractmethod


# Class LivingBeing
# This is an abstract base class that represents a living being in the game.
# Any class that will inherit from this must also implement the abstract method attack.
# 


class LivingBeing(ABC):

    # Attributes:
    #     name (str): The name of the living being. It is initialized during the object creation.
    #     health (int): The health value of the living being. It is also initialized during the object creation.
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # Methods:
    #
    #  attack(self, living_being: LivingBeing): An abstract method that must be implemented by any children class.
    #  It defines the logic of how a living being attacks another.\
    #  The method is abstract because the player and monster class, who inherit it, have different logic
    @abstractmethod
    def attack(self, living_being):
        pass

    # display_health(self): First sets the health attribute to zero if it is less than zero.
    # Then, prints the name and health of the being.
    def display_health(self):
        if self.health < 0:
            self.health = 0
        print(f"{self.name} has {self.health}hp")
