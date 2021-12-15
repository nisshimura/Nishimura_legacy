#include <stdio.h>
#include <math.h>

int main()
{
    unsigned int x;
    int i,ruizyo,a[32]={0};
    printf("word=0x");
    scanf("%x",&x);

    for (i=31;i>=0;i--)
    {
        ruizyo = pow(2, i);
        if (x >= ruizyo)
        {
            a[i] = 1;
            x = x % ruizyo;
        }
    }
    for (i = 0; i <= 31; i++)
    {
        
        if (a[i]==1)
        {
            printf("bit index = %d",i);
            break;
        }
        if (i==31)
        {
            printf("bit index = 32");
        }
    }
    return 0;
}