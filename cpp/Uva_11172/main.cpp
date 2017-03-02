#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
    int a, b, c;
    scanf("%i", &a);
    while (a--) {
        scanf("%i", &b);
        scanf("%i", &c);
        if (b < c) {
            printf("%s\n","<");
        } else if (b > c) {
            printf("%s\n",">");
        } else {
            printf("%s\n","=");
        }
    }
    return 0;
}

