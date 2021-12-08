#include <stdio.h>
int main()
{
    int a,count=0,i = 1;

    do
    {
        if (i == 1)
        {
            printf("input number:");
            scanf("%d", &a);
            if (a <= 0)
            {
                printf("Incorrect input\n");
                continue;
            }
            printf("%d is multiplication of ", a);
            if (a == 1)
            {
                printf("1\n");
                break;
            }
        }
        while (1)
        {
            if (a%i!=0&&count!=0)
            {
                printf("%d^%d ",i,count);
                i++;
                break;
            }
            else if (i == 1 || a % i != 0)
            {
                i++;
            }
            else
            {
                a /= i;
                count++;
            }
        }
        count = 0;
    } while (a!=1);
}