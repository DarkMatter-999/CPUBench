#include <stdio.h>
#include <stdbool.h>

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
      printf("%d\n", i);
    }
  }

  return 0;
}
