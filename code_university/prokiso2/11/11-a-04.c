#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    FILE *fp;
    int sentence=0,words=0,chr;

    fp = fopen("11-a-04.txt", "r");
    if (fp == NULL)
    {
        printf("open error.");
        exit(1);
    }

    while ((chr = fgetc(fp)) != EOF)
    {
        if (chr == '.')
        {
            sentence++;
        }
        if (chr == ' ')
        {
            words++;
        }
    }
    words++; //last words without ' ' or '\n'
    printf("sentence : %d\n", sentence);
    printf("words : %d\n",words);

    fclose(fp);

    return 0;
}