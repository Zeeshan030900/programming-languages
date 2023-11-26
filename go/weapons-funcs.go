package main

import (
	"fmt"
	"strconv"
	"strings"
)

func askWeaponSwitch(currentPlayer Player, chooseWeapon func(createWeapons func() []Weapon) Weapon) Player {
	fmt.Println("Would you like to switch weapons? Y/N")
	response := strings.ToUpper(getInput("input response"))
	switch {
	case response == "Y":
		chosenWeapon := chooseWeapon(createWeapons)
		return Player{
			Name:        currentPlayer.Name,
			Weapon:      chosenWeapon,
			Health:      currentPlayer.Health,
			AttackDelay: chosenWeapon.Delay,
		}
	case response == "N":
		fmt.Println("Someone loves their weapon")
	default:
		fmt.Println("Fine be that way. You're staying with your current weapon >:(")
		return currentPlayer

	}
	return currentPlayer
}
func chooseWeapon(createWeapons func() []Weapon) Weapon {
	for {

		weaponsList := createWeapons()

		fmt.Println("Choose a weapon")
		for i, weapon := range weaponsList {
			fmt.Printf("%d: name: %s, damage: %d, delay: %d\n", i, weapon.Name, weapon.Damage, weapon.Delay)
		}

		weaponIndex := getInput("weapon number")
		index, err := strconv.Atoi(weaponIndex)
		if err == nil && index >= 0 && index < len(weaponsList) {
			fmt.Println("You have chosen " + weaponsList[index].Name)
			return weaponsList[index]
		}

		fmt.Println("Not a valid weapon option. Please try again")
	}
}

func createWeapons() []Weapon {
	return []Weapon{
		{Name: "Pistol", Damage: 30, Delay: 0},
		{Name: "Shotgun", Damage: 50, Delay: 1},
		{Name: "Sub Machine Gun", Damage: 80, Delay: 2},
		{Name: "Assault Rifle", Damage: 120, Delay: 3},
		{Name: "Grenade Launcher", Damage: 170, Delay: 4},
	}
}
