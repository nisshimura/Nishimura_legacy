#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    FILE *fp;
    int count, chr;

    fp = fopen("11-a-03.txt", "r");
    if (fp == NULL)
    {
        printf("open error.");
        exit(1);
    }

    while ((chr = fgetc(fp)) != EOF)
    {
        if (count==0)
        {
            printf("name=");
            count++;
        }
        if (chr == ' '||chr=='\n')
        {
            if (count==1)
            {
                count++;
                printf(",height=");
            }
            else if (count==2)
            {
                count++;
                printf(",weight=");
            }
            else if (count==3)
            {
                count=0;
            }
        }
        printf("%c", chr);
    }
    fclose(fp);

    return 0;
}