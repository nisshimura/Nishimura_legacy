#include <stdio.h>
int main()
{
    float x,y;
    printf("Input weight of salt(g): ");
    scanf("%f", &x);
    printf("Input weight of water(g): ");
    scanf("%f", &y);
    if ((x / y) <= 0.2628){
        printf("%f (g) of salt dissolves in %f of water.",x,y);
    }
    else
    {
        printf("%f (g) of salt does not dissolves in %f of water.",x,y);
    }

    return 0;
}