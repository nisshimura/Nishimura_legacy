#include <stdio.h>
int main()
{
    int x;
    printf("Input 1st number: ");
    scanf("%d", &x);
    if (x == 1 | x == 2 | x == 3 | x == 4 | x == 5 | x == 6 | x == 7 | x == 8 | x == 9){
        printf("%d is one of disit positive integer.", x);
    }else {
        printf("%d is not one of disit positive integer",x);
    }

    return 0;
}