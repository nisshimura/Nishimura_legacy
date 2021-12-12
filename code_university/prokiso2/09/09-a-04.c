#include <stdio.h>
int counter(char k[],int max)
{
    int i,count=0;
    
    for (i=0;i<max;i++)
    {
        switch (k[i])
        {
        case 'a':
        case 'i':
        case 'u':
        case 'e':
        case 'o':
            count++;
        
        default:
            break;
        }
    }
    return count;
}
int main()
{
    char d,k[10];
    int i,result;

    printf("input 10 characters:");
    for (i = 0; i < 10; i++)
    {
        d = getchar();
        if (d == '\n')
        {
            break;
        }
        k[i] = d;
    }
    result = counter(k,10);
    printf("count:%d\n", result);
}