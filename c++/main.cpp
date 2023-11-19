#include "structs.cpp"
#include <cctype>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <ostream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

using namespace std;

Player introduction() {
  cout << "Welcome to Manchester Metropolitan University. We have been taken "
          "over by reports sadly. Thanks to the A.I students >:0"
       << endl;
  cout << "What is your name?";
  Player player;
  cin >> player.name;
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
  cin >> weaponIndex;
  if (!cin) {
    cin.clear();
    cin.ignore(40, '\n');
    throw std::invalid_argument("Not a valid option");
  };

  if (weaponIndex >= 0 && weaponIndex < 5) {
    player.weapon = weapons[weaponIndex];
    player.attackDelay = player.weapon.delay;
  } else {
    throw std::invalid_argument("Not a valid option");
  }
}

void printHealth(string name, int &health) {
  health = (health < 0) ? 0 : health;
  cout << name << " is on " << health << "hp" << endl;
  std::this_thread::sleep_for(std::chrono::seconds(3));
}

bool switchWeapon() {
  char input;

  cout << "Do you want to switch weapons?" << endl;
  cout << "Press Y or y if so" << endl;
  cin >> input;

  cin.clear();
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

  return input == 'Y' || input == 'y';
}

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
        cout << "You have decided not to switch weapons.";
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
