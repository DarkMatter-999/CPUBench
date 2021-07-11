#include <iostream>

int main(int argc, char const *argv[]) {
  for(int i = 2; i < 100000; i++){
    bool prime = true;

    for(int j = 2; j*j <= i; j++){
        if(i % j == 0){
          prime = false;
          break;
        }
    }
    if(prime){
      std::cout << i << std::endl;

    }
  }

  return 0;
}
