from living_being_class import LivingBeing


class Monster(LivingBeing):
    def __init__(self, name, health, attack_damage):
        super().__init__(name, health)
        self.attackdamage = attack_damage

    def attack(self, player):
        print(f"{self.name} attacked {player.name}. Attack did {self.attackdamage} amount of damage")
        player.health -= self.attackdamage
