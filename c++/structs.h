
#ifndef MYSTRUCT_H
#define MYSTRUCT_H

#include <string>

struct Weapon {
  std::string name;
  int damage;
  int delay;
};

struct Player {
  std::string name;
  int health;
  int attackDelay;
  Weapon weapon;
};

struct Monster {
  std::string name;
  int health;
  int damage;
};

#endif
