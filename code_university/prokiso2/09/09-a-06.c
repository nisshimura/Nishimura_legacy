#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Input a:");
    scanf("%d", &a);

    printf("Input b:");
    scanf("%d", &b);
    printf("%d + %d = %d\n",a,b,a+b);
    printf("%d - %d = %d\n", a, b, a - b);
    printf("%d * %d = %d\n", a, b, a * b);
    printf("%d / %d = %d\n", a, b, a / b);

    printf("%x & %x = 0x%x\n", a, b, a & b);
    printf("%x | %x = 0x%x\n", a, b, a | b);
    printf("%x ^ %x = 0x%x\n", a, b, a ^ b);
    printf("%x << %x = 0x%x\n", a, b, a << b);
    printf("%x >> %x = 0x%x\n", a, b, a >> b);
}