import random
import time
from abc import ABC, abstractmethod


class Game:
    gameStates = {"PLAY": 1, "END": 2}

    def __init__(self, gamestate):
        self.gameState = gamestate
        self.floor = 0

    def introduction(self, weapons):
        print("Welcome to Manchester Metropolitan University")
        print("The university has been taken over by AI robots. Thanks to the A.I students >:O")

        name = input("What is your name? ")

        print(f"Hello, {name}")
        p = Player(name, 200)
        p.choose_weapon(weapons)
        return p

    def check_to_continue(self, p):
        answered = False
        while answered is not True:
            try:
                playerinput = input(
                    f"You are on floor {self.floor}. You have {p.health}hp.\nDo you want to progress?\nY/N"
                )
                if playerinput.upper() != "Y" and playerinput.upper() != "N":
                    raise NameError
                return playerinput.upper()
            except NameError:
                print("Not a valid response")

    def progress(self, player):

        monster = self.create_random_monster()
        while player.health > 0 and monster.health > 0:

            player.attack(monster)
            monster.display_health()
            time.sleep(3)

            if monster.health > 0:
                monster.attack(player)
                player.display_health()
                time.sleep(3)
            else:
                print(f"{monster.name} has died")
                time.sleep(3)

    def create_random_monster(self):
        monster_list = [Monster("Terminator", 50, 10),
                        Monster("Cyber demon", 60, 15),
                        Monster("Annihilator", 70, 20),
                        Monster("Doomsday Bot", 80, 25)]

        return random.choice(monster_list)

    @staticmethod
    def create_initial_weapons():
        return {1: Weapon("Pistol", 30, 0),
                2: Weapon("Shotgun", 50, 1),
                3: Weapon("Smg", 70, 2),
                4: Weapon("Assault Rifle", 90, 3),
                5: Weapon("RPG", 100, 4)
                }

    def game_over(self):
        print(f"Game Over.\nYou cleared {game.floor} floors")


class Weapon:
    def __init__(self, name, damage, delay):
        self.name = name
        self.damage = damage
        self.delay = delay


class LivingBeing(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, living_being):
        pass

    def display_health(self):
        if self.health < 0:
            self.health = 0
        print(f"{self.name} has {self.health}hp")


class Player(LivingBeing):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.weapon = None
        self.attackDelay = 0

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
                print("Invalid input. Please enter a number.")
                print()


class Monster(LivingBeing):
    def __init__(self, name, health, attackDamage):
        super().__init__(name, health)
        self.attackdamage = attackDamage

    def attack(self, player):
        print(f"{self.name} attacked {player.name}. Attack did {self.attackdamage} amount of damage")
        player.health -= self.attackdamage


if __name__ == '__main__':

    game = Game(Game.gameStates["PLAY"])

    weapons = game.create_initial_weapons()

    player = game.introduction(weapons)

    while game.gameState != game.gameStates["END"]:

        if player.health < 0:
            print(f"{player.name} has died")
            game.gameState = game.gameStates["END"]

        elif game.floor == 10:
            print("You have reached the end and saved the university :D")
            game.gameState = game.gameStates["END"]

        else:
            if game.check_to_continue(player) == "Y":

                try:
                    switch_weapon_check = input("Do you want to change weapon? Y/N")
                    print()
                    if switch_weapon_check.upper() != "Y" and switch_weapon_check.upper() != "N":
                        raise NameError
                    elif switch_weapon_check.upper() == "Y":
                        player.choose_weapon(weapons)

                except NameError:
                    print("Fine. You're sticking with your previous weapon >:(")

                finally:
                    game.progress(player)
                    if player.health > 0:
                        game.floor += 1

            else:
                game.gameState = game.gameStates["END"]

    game.game_over()
