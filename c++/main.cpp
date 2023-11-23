#include "funcs.h"
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

using namespace std;

int main() {

  Player player = introduction();

  Weapon weapons[5] = {{"Pistol", 30, 0},
                       {"Shotgun", 50, 1},
                       {"Sub Machine Gun", 80, 2},
                       {"Assault Rifle", 120, 3},
                       {"Grenade Launcher", 170, 4}};

  cout << "Select a weapon number" << endl;
  displayWeapons(weapons);

  bool weaponChosen = false;
  std::cout << "Select a weapon:\n";

  do {
    try {

      cout << "Please Choose a weapon number";

      chooseWeapon(weapons, player);

      weaponChosen = true;
    } catch (std::invalid_argument &e) {
      std::cout << e.what() << endl;
    }
  } while (!weaponChosen);

  Monster monsterList[4] = {{"Terminator", 50, 10},
                            {"Cyber demon", 60, 15},
                            {"Annihilator", 70, 20},
                            {"Doomsday Bot", 80, 25}};

  int randomIndex = rand() % 4;
  Monster monster = monsterList[randomIndex];

  int floors = 1;
  bool keepPlaying = true;

  do {

    printHealth(monster.name, monster.health);
    if (monster.health == 0) {
      std::cout << monster.name + " has died" << endl;

      floors += 1;
      std::this_thread::sleep_for(std::chrono::seconds(3));

      std::cout << player.name + " is on floor " << floors << endl;
      if (floors == 10) {
        keepPlaying = false;
        break;
      }

      if (switchWeapon()) {
        displayWeapons(weapons);
        try {
          cout << "Please Choose a weapon number";

          chooseWeapon(weapons, player);

          weaponChosen = true;
        } catch (std::invalid_argument &e) {
          std::cout
              << "Fine. Be that way. You're sticking with the same weapon >:("
              << endl;
        }

      } else {
        cout << "You have decided not to switch weapons." << endl;
      }

      randomIndex = rand() % 4;
      monster = monsterList[randomIndex];
    }

    printHealth(player.name, player.health);
    if (player.health == 0) {
      std::cout << player.name + " has died" << endl;
      keepPlaying = false;
      break;
    }

    if (player.attackDelay == 0) {
      cout << player.name + " has done " << player.weapon.damage
           << " damage to " + monster.name << endl;

      monster.health -= player.weapon.damage;
      player.attackDelay = player.weapon.delay;
    } else {

      cout << player.name + " has to wait " << player.attackDelay
           << " before attacking" << endl;
      player.attackDelay -= 1;
    }
    std::this_thread::sleep_for(std::chrono::seconds(3));

    cout << monster.name + " has done " << monster.damage
         << " damage to " + player.name << endl;
    player.health -= monster.damage;

    std::this_thread::sleep_for(std::chrono::seconds(3));

  } while (keepPlaying);

  cout << "Game Over" << endl;
  cout << "You reached " << floors << " floors." << endl;

  return 0;
}
