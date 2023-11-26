from game_class import Game, Gamestates

if __name__ == '__main__':

    game = Game()

    weapons = game.create_initial_weapons()

    player = game.introduction(weapons)

    while game.gameState != Gamestates.END:

        game.check_game_state(player)
        if game.gameState == Gamestates.END:
            break

        game.check_to_continue(player)
        if game.gameState == Gamestates.END:
            break

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

game.game_over()
