#include <stdio.h>

int main()
{
    char d,target[20];
    int i, count = 0;
    for (i=0;i<20;i++)
    {
        d = getchar();
        if (d=='\n')
        {
            break;
        }
        target[i] = d;
        count++;
    }

    for (i=0; i <= count/2; i++)
    {
        if (target[i]!=target[count-1-i])
        {
            printf("This str is not a palindrome");
            break;
        }
        if (count==1||i==count/2)
        {
            printf("This str is a palindrome");
        }

    }
}