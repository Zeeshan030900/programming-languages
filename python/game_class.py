import random
import time
from enum import Enum, unique

from monster_class import Monster
from player_class import Player
from weapon_class import Weapon


# Enum `Gamestates`
#  This class is used to define the states of the game.
#  PLAY: Represents the state of the game where the game is in progress.
#  END: Represents the state of the game where the game has ended.

class Gamestates(Enum):
    PLAY = 1
    END = 2


# Class Game
#
# This is the main class handling the game flow.
#
class Game:
    #    Attributes:
    #     gameState (GameState) : It represents the state of the game- whether it is in progress or has ended.
    #     floor (int) : It holds the floor/level of the game the player has reached. Initialized as 1.

    def __init__(self):
        self.gameState = Gamestates.PLAY
        self.floor = 1

    #   Methods:
    #
    # introduction(self, weapons: dict) -> Player:
    #  Begins the game by greeting the user, asking for their name and setting up their weapon.
    #  Creates a player instance, based on the user input
    #  Returns the player instance
    #  This is a static method

    @staticmethod
    def introduction(weapons):
        print("Welcome to Manchester Metropolitan University")
        print("The university has been taken over by AI robots. Thanks to the A.I students >:O")

        name = input("What is your name? ")

        print(f"Hello, {name}")
        p = Player(name, 200)
        p.choose_weapon(weapons)
        return p

    #  check_to_continue(self, p: Player) -> str:
    #   Asks for the player's choice to progress the game.
    #   Will continue to ask until the player gives a valid input  
    #   Returns the player's input.

    def check_to_continue(self, p):
        print(f"You are on floor {self.floor}. You have {p.health}hp.")
        answered = False
        while answered is not True:
            try:
                playerinput = input(
                    "Do you want to progress?\nY/N\n"
                )
                if playerinput.upper() != "Y" and playerinput.upper() != "N":
                    raise ValueError
                return playerinput.upper()
            except ValueError:
                print("Not a valid response")

    #  progress(self, player: Player) :
    #    Handles the game progression.
    #    The create_random_monster method is called.
    #    The player and the monster decrease each others health inside a while loop.  
    #    Continues until either the player or the monster's health goes below 0.

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

    # create_random_monster(self) -> Monster :
    #  Creates a random Monster for the player to face off against from a predefined list.
    #  This is a static method 
    @staticmethod
    def create_random_monster():
        monster_list = [Monster("Terminator", 50, 10),
                        Monster("Cyber demon", 60, 15),
                        Monster("Annihilator", 70, 20),
                        Monster("Doomsday Bot", 80, 25)]

        return random.choice(monster_list)

    # create_initial_weapons(self) -> dict :
    #  Creates and returns the initial set of weapons for the game. This is a static method.

    @staticmethod
    def create_initial_weapons():
        return {1: Weapon("Pistol", 30, 0),
                2: Weapon("Shotgun", 50, 1),
                3: Weapon("Smg", 80, 2),
                4: Weapon("Assault Rifle", 120, 3),
                5: Weapon("RPG", 150, 4)
                }

    # game_over
    #  Ends the game and displays how many floors the player cleared in the game.
    def game_over(self):
        print(f"Game Over.\nYou cleared {self.floor} floors")
