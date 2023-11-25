from living_being_class import LivingBeing


# Class Player
# Inherits from the LivingBeing class.
# Represents a player in the game with certain functionalities such as attacking and choosing weapons.
class Player(LivingBeing):

    # Attributes:
    # - name (str): The name of the Player
    # - health (int): The Player's health points. Inherited from LivingBeing class.
    # - attackDelay (int): The delay for the Player's attack. Equal to 0 by default.
    # - weapon (object): The object representing the weapon of the Player.

    def __init__(self, name, health):
        super().__init__(name, health)
        self.attackDelay = 0
        self.weapon = None

    # Method "attack" is used for the Player to attack a Monster.
    # If attackDelay is 0, the Player can attack; otherwise, it has to wait the required number of turns.
    def attack(self, monster):
        if self.attackDelay == 0:
            print(f"{self.name} attacked {monster.name} with a {self.weapon.name}",
                  f"Attack did {self.weapon.damage} amount of damage")
            monster.health -= self.weapon.damage
            self.attackDelay = self.weapon.delay

        else:
            print(f"{self.name} has {self.attackDelay} turns to wait before attacking")
            self.attackDelay -= 1

    # Method "choose_weapon" allows the Player to choose a weapon from the given list of weapons.
    # It also sets the attackDelay according to the chosen weapon.
    def choose_weapon(self, weapons):
        print("Choose a weapon from this list:")
        for index, weapon in weapons.items():
            print(f"{index}: name: {weapon.name} damage: {weapon.damage} delay: {weapon.delay}")

        while True:
            try:
                weaponindex = int(input("Enter the number of your chosen weapon: "))
                if weaponindex in weapons:
                    self.weapon = weapons[weaponindex]
                    self.attackDelay = weapons[weaponindex].delay
                    print()
                    return
                else:
                    print("That is not an option.")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
