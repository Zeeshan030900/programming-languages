from living_being_class import LivingBeing


class Player(LivingBeing):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.attackDelay = 0
        self.weapon = None

    def attack(self, monster):
        if self.attackDelay == 0:
            print(f"{self.name} attacked {monster.name} with a {self.weapon.name}",
                  f"Attack did {self.weapon.damage} amount of damage")
            monster.health -= self.weapon.damage
            self.attackDelay = self.weapon.delay

        else:
            print(f"{self.name} has {self.attackDelay} turns to wait before attacking")
            self.attackDelay -= 1

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
