#include <stdio.h>

int main()
{
    int a,count,total=0;

    while (1)
    {
        printf("input a positive integer:");
        scanf("%d", &a);
        if (a<0)
        {
            printf("Error:invalid input\n");
            continue;
        }
        else if (a==0||count==4)
        {
            printf("total:%d",total);
            break;
        }
        else
        {
            count++;
            total+=a;
        }
    }
    return 0;
}