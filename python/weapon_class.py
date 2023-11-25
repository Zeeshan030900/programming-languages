# Class Weapon
# This class represents a weapon object in a game. It initializes three attributes: name, damage and delay.
# This class is implemented by the player class
class Weapon:
    # Attributes:
    #     name : str
    #         The name of the weapon.
    #     damage : int
    #         The amount of damage that the weapon can cause.
    #     delay : int
    #         The delay (in turns) between the next use of the weapon.
    # 
    def __init__(self, name, damage, delay):
        self.name = name
        self.damage = damage
        self.delay = delay
