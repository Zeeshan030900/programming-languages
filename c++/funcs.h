#ifndef FUNCS_H
#define FUNCS_H

#include "structs.h"
#include <cctype>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <ostream>
#include <stdexcept>
#include <string>
#include <thread>

Player introduction() {
  std::cout
      << "Welcome to Manchester Metropolitan University. We have been taken "
         "over by reports sadly. Thanks to the A.I students >:0"
      << std::endl;

  std::cout << "What is your name?" << std::endl;

  Player player;
  std::cin >> player.name;
  player.health = 200;
  return player;
};

void displayWeapons(Weapon weapons[]) {
  for (int i = 0; i < 5; ++i) {
    std::cout << i << ": Name: " + weapons[i].name
              << " Damage: " << weapons[i].damage
              << " Attack Delay: " << weapons[i].delay << '\n';
  }
};

void chooseWeapon(Weapon weapons[], Player &player) {
  int weaponIndex;
  std::cout << "Please Choose a weapon number";
  std::cin >> weaponIndex;
  if (!std::cin) {
    std::cin.clear();
    std::cin.ignore(40, '\n');
    throw std::invalid_argument("Not a valid option");
  };

  if (weaponIndex >= 0 && weaponIndex < 5) {
    player.weapon = weapons[weaponIndex];
    player.attackDelay = player.weapon.delay;
  } else {
    throw std::invalid_argument("Not a valid option");
  }
}

void printHealth(std::string name, int &health) {
  health = (health < 0) ? 0 : health;
  std::cout << name << " is on " << health << "hp" << std::endl;
  std::this_thread::sleep_for(std::chrono::seconds(3));
}

bool switchWeapon() {
  char input;

  std::cout << "Do you want to switch weapons?" << std::endl;
  std::cout << "Press Y or y if so" << std::endl;
  std::cin >> input;

  std::cin.clear();
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

  return input == 'Y' || input == 'y';
}

void processPlayerTurn(Player &player, Monster &monster) {
  if (player.attackDelay == 0) {
    std::cout << player.name + " has done " << player.weapon.damage
              << " damage to " + monster.name << std::endl;
    monster.health -= player.weapon.damage;
    player.attackDelay = player.weapon.delay;
  } else {
    std::cout << player.name + " has to wait " << player.attackDelay
              << " before attacking" << std::endl;
    player.attackDelay -= 1;
  }
  std::this_thread::sleep_for(std::chrono::seconds(3));
}

void processMonsterTurn(Monster &monster, Player &player) {
  std::cout << monster.name + " has done " << monster.damage
            << " damage to " + player.name << std::endl;
  player.health -= monster.damage;
  std::this_thread::sleep_for(std::chrono::seconds(3));
}

bool processMonsterDeath(Monster &monster, int &floors) {
  std::cout << monster.name + " has died" << std::endl;

  floors += 1;
  std::this_thread::sleep_for(std::chrono::seconds(3));

  std::cout << "Player is on floor " << floors << std::endl;
  return floors == 10;
}

#endif
