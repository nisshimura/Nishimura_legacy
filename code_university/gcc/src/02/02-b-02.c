#include <stdio.h>
int main()
{
    int x, y;
    printf("Input a: ");
    scanf("%d", &x);
    printf("Input b: ");
    scanf("%d", &y);

    int sum = x + y;
    int sub = x - y;
    int multi = x * y;
    float div = (float)x / (float)y; 
    
    printf("%d + %d = %d\n", x, y, x+y);
    printf("%d - %d = %d\n", x, y, x-y);
    printf("%d x %d = %d\n", x, y, x*y);
    printf("%d / %d = %f\n", x, y, div);


    return 0;
}