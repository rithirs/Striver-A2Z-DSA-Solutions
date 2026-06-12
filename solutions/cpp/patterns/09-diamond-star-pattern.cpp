#include <iostream>
using namespace std;
int main() {
    for(int i = 0, n = 5; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) cout << " ";
        for(int j = 0; j < 2 * i + 1; j++) cout << "*";
        cout << endl;
    }
    for(int i = 4; i > 0; i--) {
        for(int j = 0; j < 5 - i; j++) cout << " ";
        for(int j = 0; j < 2 * i - 1; j++) cout << "*";
        cout << endl;
    }
    return 0;
}