#include <stdio.h>

int greatest_common_division(int a ,int b)
{
    if (a%b==0|b%a==0)
    {
        return b;
    }
    if (a>b)
    {
        greatest_common_division(b,a%b);
    }
    else
    {
       greatest_common_division(a,b%a); 
    }
}
int main()
{
    int a,b;
    printf("input two integer:");
    scanf("%d %d",&a,&b);
    printf("greatest common division is %d",greatest_common_division(a,b));
    return 0;
}