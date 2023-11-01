package main

type Player struct {
	Name        string
	Weapon      Weapon
	Health      int
	AttackDelay int
}

type Weapon struct {
	Name   string
	Damage int
	Delay  int
}

type Monster struct {
	Name   string
	Damage int
	Health int
}
