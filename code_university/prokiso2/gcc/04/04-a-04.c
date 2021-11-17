#include <stdio.h>
int main()
{
    int x,*a;
    printf("input an integer:");
    scanf("%d", &x);
    a = &x;
    printf("address of a is %p\n", a);
    printf("value of a is %d\n", x);
}