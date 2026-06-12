#include <stdio.h>
int main(){
    for(int i = 0, n = 5; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) printf(" ");
        for(int j = 0; j < 2 * i + 1; j++) printf("*");
        printf("\n");
    }
    return 0;
}