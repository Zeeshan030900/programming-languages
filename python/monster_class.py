from living_being_class import LivingBeing


# Class Monster
# Inherits from the 'LivingBeing' class. It represents the monsters within the game.
# Monsters have the same attributes as any living being, such as name and health, but also have specific attack damage,
# which will be used to hurt other players.
class Monster(LivingBeing):

    # Attributes:
    # - name (str): Represents the name of the monster.
    # - health (int or float): Represents the health points of the monster. Decreases when the monster gets attacked.
    # - attack_damage (int or float): Represents the amount of damage the monster can inflict on the player.
    def __init__(self, name, health, attack_damage):
        super().__init__(name, health)
        self.attackdamage = attack_damage

    # Methods:
    # - attack(self, player): Inflicts damage to the player equal to the monster's attack damage.
    # This also prints a message about the attack.
    def attack(self, player):
        print(f"{self.name} attacked {player.name}. Attack did {self.attackdamage} amount of damage")
        player.health -= self.attackdamage
