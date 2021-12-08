#include <stdio.h>
int main()
{
    int a, syo;
    char dic[][6] = {
                    "zero",
                    "ichi",
                    "ni",
                    "san",
                    "yon",
                    "go",
                    "roku",
                    "nana",
                    "hachi",
                    "kyu",
                    "ju",
                    "hyaku",
                    "sen",
                    "minus"
                    };

    do
    {
        printf("input number:");
        scanf("%d", &a);
        if (a < -9999 || a>9999)
        {
            printf("Input range is -9999 to 9999\n");
            continue;
        }
        if (a == 0)
        {
            printf("%s", dic[0]);
            break;
        }
        while (1)
        {
            if (a==0)
            {
                break;
            }
            else if (a<0)
            {
                printf("%s ",dic[13]);
                a *= -1;
            }
            else if (a>=1000)
            {
                printf("%s %s ",dic[a/1000],dic[12]);

                a %= 1000;
            }
            else if (a >= 100)
            {
                printf("%s %s ", dic[a / 100], dic[11]);
                a %= 100;
            }
            else if (a >= 10)
            {
                printf("%s %s ", dic[a / 10], dic[10]);
                a %= 10;
            }
            else if (a >= 1)
            {
                printf("%s ", dic[a / 1]);
                break;
            }
        }
        printf("\n");
    } while (a != 1);
}