#include <stdio.h>
#include <stdlib.h>

void find_zero(char *a, int max)
{
    int i;
    printf("Zero in ");
    for (i=0;i<max;i++)
    {
        
        if (a[i]=='0')
        {
            printf("%d ",i);
        }
    }
}
int main()
{
    char d, *k;
    int count=0, result;

    k = (char *)malloc(sizeof(char));
    while (1)
    {
        d = getchar();
        k = (char *)realloc(k,sizeof(char));
        if (d == '\n')
        {
            break;
        }
        k[count] = d;
        count++;
    }
    find_zero(k,count);
    free(k);
    return 0;
}