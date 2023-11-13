#include "structs.cpp"
#include <iostream>
#include <iterator>
#include <ostream>
#include <stdexcept>
#include <string>
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
    std::cout << i << ": Name: " << weapons[i].name
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
  } else {
    throw std::invalid_argument("Not a valid option");
  }
}

int main() {

  Player player = introduction();

  Weapon weapons[5] = {{"Pistol", 30, 0},
                       {"Shotgun", 50, 1},
                       {"Sub Machine Gun", 80, 2},
                       {"Assault Rifle", 120, 3},
                       {"Grenade Launcher", 170, 4}};

  cout << "Select a weapon" << endl;
  displayWeapons(weapons);

  bool weaponChosen = false;
  std::cout << "Select a weapon:\n";

  do {
    try {
      cout << "Please Choose a weapon index";
      chooseWeapon(weapons, player);
      weaponChosen = true;
      std::cout << player.weapon.name << endl;
    } catch (std::invalid_argument &e) {
      cout << e.what() << endl;
    }
  } while (!weaponChosen);
  return 0;
}
