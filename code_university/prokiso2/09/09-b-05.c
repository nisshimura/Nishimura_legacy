#include <stdio.h>
#include <math.h> 

int main()
{
    int ruizyo,i,ascii2[8]={0};
    int ascii10 = getchar();
    for (i=7;i>=0;i--)
    {
        ruizyo = pow(2, i);
        if (ascii10 >= ruizyo)
        {
            ascii2[7-i] = 1;
            ascii10 = ascii10 % ruizyo;
        }
        
        
    }
    for (i = 0; i <= 7; i++)
    {
        printf("%d",ascii2[i]);
    }
}