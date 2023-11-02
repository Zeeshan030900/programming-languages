#include <iostream>
#include <string>
#include "structs.cpp"

using namespace std;

Player introduction(){
 cout << "Welcome to Manchester Metropolitan University. We have been taken over by reports sadly. Thanks to the A.I students >:0" << endl;
 cout << "What is your name?";
 Player player; 
 cin >> player.name;
 return player;
}

int main(){
  Player a = introduction();
  cout << a.name;
  return 0;
}
