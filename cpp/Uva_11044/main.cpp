#include <stdio.h>
using namespace std;
int main() {
    int a, b, c;
    scanf("%i", &a);
    while (a--) {
        scanf("%i", &b);
        scanf("%i", &c);
        b /= 3;
        c /= 3;
        printf("%i\n", (b*c));
    }
    return 0;
}

