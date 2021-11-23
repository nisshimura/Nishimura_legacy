#include <stdio.h>
int main()
{   
    float x,y;
    printf("input two integer:");
    scanf("%f %f", &x, &y);
    printf("%10.4f\n", x+y);
    printf("%10.4f\n", x-y);
    printf("%10.4f\n", x*y);
    printf("%10.4f\n", x/y);
    return 0;
}