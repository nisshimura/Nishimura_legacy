#include <stdio.h>
int main()
{
    int a,i=0;
    printf("input number:");
    scanf("%d", &a);
    do
    {
        if (a <= 0)
        {
            printf("Incorrect input\n");
            continue;
        }
        if (i==0)
        {
            printf("%d is divisibel by ",a);
        }
        i++;
        if (a%i==0)
        {
            printf("%d ",i);
        }
    }
    while (i<a);

}