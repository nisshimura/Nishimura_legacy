#include <stdio.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    char s1[MAX_LINE],s2[MAX_LINE];
    printf("input first string : ");
    fgets(s1,MAX_LINE,stdin);
    printf("input second string : ");
    fgets(s2,MAX_LINE,stdin);
    if (strcmp(s1,s2)==0)
    {
        printf("same.");
    }
    else
    {
        printf("different.");
    }

    return 0;
}