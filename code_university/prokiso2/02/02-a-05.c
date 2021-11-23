#include <stdio.h>
int main()
{   
    float x,y;
    printf("Input 1st number: ");
    scanf("%f", &x);
    printf("Input 2st number: ");
    scanf("%f", &y);
    int z = x + y;
    printf("Result is: %d", z);
    return 0;
}