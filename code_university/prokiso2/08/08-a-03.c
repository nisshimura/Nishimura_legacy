#include <stdio.h>

int main()
{
    char ans;

    while (1)
    {
        printf("Please help me!\n");
        printf("input y or n:");
        scanf("%c", &ans);
        if (ans == 'y')
        {
            printf("Thank you!\n");
            break;
        }
        else if (ans == 'n')
        {
            printf("Huh?\n");
        }
        scanf("%c", &ans);
    }
    return 0;
}