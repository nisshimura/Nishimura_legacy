#include <stdio.h>

int main()
{
    int a,i=0,result=0;
    printf("input a positive integer:");
    scanf("%d", &a);

    while (i<=a)
    {
        result += i;
        i++;
    }
    printf("total:%d",result);
    return 0;
}