package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {

	player := introduction()

	fmt.Println("Hello " + player.Name)
	fmt.Println(fmt.Sprintf("You reached %d floors", playGame(player, createRandomMonster(), 1)))
	fmt.Println("Game Over")
}

func introduction() Player {
	fmt.Println("Welcome to Manchester Metropolitan University")
	fmt.Println("The university has been taken over by AI robots. Thanks to the A.I students >:O")
	fmt.Println("What is your name")

	name := getInput("name")
	weapon := chooseWeapon(createWeapons)

	return Player{Name: name, Weapon: weapon, Health: 200}
}

/*
	Function to retrieve user input. Made it into a generic function because user input will be needed in multiple parts of the code
	@param inputType. This is to tell the user to enter a certain input if they try to enter a blank. E.G name.
*/
func getInput(inputType string) string {
	reader := bufio.NewReader(os.Stdin)
	for {
		consoleText := fmt.Sprintf("Please enter a %s: ", inputType)

		fmt.Println(consoleText)
		input, _ := reader.ReadString('\n')
		trimmedInput := strings.TrimSpace(input)
		if trimmedInput != "" {
			return trimmedInput
		}
	}
}

func playGame(player Player, monster Monster, floor int) int {

	displayHealth := func(name string, health int) string {
		if health < 0 {
			return fmt.Sprintf("%s is on 0hp\n%s has died", name, name)
		} else {
			return fmt.Sprintf("%s is on %dhp", name, health)
		}
	}

	fmt.Println(displayHealth(player.Name, player.Health))
	time.Sleep(3 * time.Second)
	if player.Health <= 0 {
		return floor
	}

	fmt.Println(displayHealth(monster.Name, monster.Health))
	time.Sleep(3 * time.Second)
	if monster.Health <= 0 {
		progrssFloorText := fmt.Sprintf("%s has cleared floor %d. Now moving to floor %d", player.Name, floor, floor+1)
		fmt.Println(progrssFloorText)
		askWeaponSwitch(player, chooseWeapon)
		return playGame(player, createRandomMonster(), floor+1)
	}

	damagedPlayer, damagedMonster := tradeAttacks(player, monster)

	return playGame(damagedPlayer, damagedMonster, floor)
}

func tradeAttacks(player Player, monster Monster) (Player, Monster) {

	decrementAttackDelay := func(player Player) int {
		if player.AttackDelay == 0 {
			return player.Weapon.Delay
		}
		return player.AttackDelay - 1
	}

	damagedPlayer := Player{Name: player.Name,
		Health:      player.Health - monster.Damage,
		AttackDelay: player.AttackDelay,
		Weapon:      player.Weapon,
	}
	damageText := fmt.Sprintf("%s took %d damage", damagedPlayer.Name, monster.Damage)
	fmt.Println(damageText)
	time.Sleep(3 * time.Second)

	if damagedPlayer.AttackDelay <= 0 {
		damagedMonster := Monster{Name: monster.Name,
			Health: monster.Health - damagedPlayer.Weapon.Damage,
			Damage: monster.Damage,
		}
		damageText := fmt.Sprintf("%s took %d damage", monster.Name, player.Weapon.Damage)
		fmt.Println(damageText)
		time.Sleep(3 * time.Second)

		newPlayer := Player{Name: damagedPlayer.Name,
			AttackDelay: decrementAttackDelay(damagedPlayer),
			Health:      damagedPlayer.Health,
			Weapon:      damagedPlayer.Weapon,
		}

		return newPlayer, damagedMonster
	}

	playerDelayText := fmt.Sprintf("%s has got %d amount of turns before attacking", damagedPlayer.Name, damagedPlayer.AttackDelay)
	fmt.Println(playerDelayText)

	newPlayer := Player{Name: damagedPlayer.Name,
		AttackDelay: decrementAttackDelay(damagedPlayer),
		Health:      damagedPlayer.Health,
		Weapon:      damagedPlayer.Weapon,
	}

	return newPlayer, monster
}
