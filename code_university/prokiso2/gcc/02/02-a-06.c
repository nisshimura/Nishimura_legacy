#include <stdio.h>
int main()
{
    int x, y;
    printf("Input 1st number: ");
    scanf("%d", &x);
    printf("Input 2st number: ");
    scanf("%d", &y);
    if (x == y){
        printf("Two numbers are equal.");
    }else if (x < y) {
        printf("%d is larger than %d",y,x);
    }else if (x > y) {
        printf("%d is larger than %d",x,y);
    }
    return 0;
}