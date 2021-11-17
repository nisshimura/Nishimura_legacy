#include <stdio.h>
int sum(int *x ,int *y)
{   
    int result;
    result = *x + *y;
    return result;
}
int main()
{
    int a, b;
    printf("input 2 integers :");
    scanf("%d %d", &a, &b);
    printf("%d + %d = %d\n", a, b, sum(&a, &b));
    return 0;
}