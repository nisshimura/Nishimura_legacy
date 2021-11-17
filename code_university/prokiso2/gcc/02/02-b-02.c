#include <stdio.h>
int main()
{
    float x, y;
    printf("Input a: ");
    scanf("%f", &x);
    printf("Input b: ");
    scanf("%f", &y);

    int sum = x / y;
    int sub = x - y;
    int multi = x * y;
    int div = x / y; 
    printf("%f + %f = %d\n", x, y, sum);
    printf("%f - %f = %d\n", x, y, sub);
    printf("%f x %f = %d\n", x, y, multi);
    printf("%f / %f = %d\n", x, y, div);


    return 0;
}