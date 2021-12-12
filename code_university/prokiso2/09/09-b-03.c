#include <stdio.h>

int main()
{
    int ascii;
    char text;
    while ((text = getchar()) != EOF)
    {
        if (text!='\n')
        {
            printf("%d\n", text);
        }
    } 
}