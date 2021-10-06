#include <iostream>
using namespace std;
int addition(int a, int b) {
  return (a + b);
}

int returnIncrement(int x){
 return (++x);
}

bool isEqual(int X, int Y){
  if (X == Y or Y == X){
    return true;
  }
}
int main(){
  cout << addition(3, 2) << endl;
  cout << returnIncrement(1) << endl;
  cout << isEqual(1,1) << endl;
  cout << isEqual(1,2) << endl;

}


