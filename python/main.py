from game_class import Game, Gamestates

if __name__ == '__main__':

    game = Game()

    weapons = game.create_initial_weapons()

    player = game.introduction(weapons)

    while game.gameState != Gamestates.END:

        if player.health < 0:
            print(f"{player.name} has died")
            game.gameState = Gamestates.END

        elif game.floor == 10:
            print("You have reached the end and saved the university :D")
            game.gameState = Gamestates.END

        else:
            if game.check_to_continue(player) == "Y":

                try:
                    switch_weapon_check = input("Do you want to change weapon? Y/N \n")
                    if switch_weapon_check.upper() != "Y" and switch_weapon_check.upper() != "N":
                        raise ValueError
                    elif switch_weapon_check.upper() == "Y":
                        player.choose_weapon(weapons)

                except ValueError:
                    print("Fine. You're sticking with your previous weapon >:(")

                finally:
                    game.progress(player)
                    if player.health > 0:
                        game.floor += 1

            else:
                game.gameState = Gamestates.END

    game.game_over()
