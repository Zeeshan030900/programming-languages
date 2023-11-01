package main

import (
	"math/rand"
	"time"
)

func createRandomMonster() Monster {
	monsterList := []Monster{
		{Name: "Terminator", Health: 50, Damage: 10},
		{Name: "Cyber demon", Health: 60, Damage: 15},
		{Name: "Annihilator", Health: 70, Damage: 20},
		{Name: "Doomsday Bot", Health: 80, Damage: 25},
	}

	rand.Seed(time.Now().UnixNano())
	randomIndex := rand.Intn(len(monsterList))
	return monsterList[randomIndex]
}
