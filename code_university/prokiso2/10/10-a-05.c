#include <stdio.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    char s1[MAX_LINE],s2[MAX_LINE],s3[MAX_LINE],max[MAX_LINE];
    printf("input string (1): ");
    fgets(s1,MAX_LINE,stdin);
    printf("input string (2): ");
    fgets(s2,MAX_LINE,stdin);
    printf("input string (3): ");
    fgets(s3,MAX_LINE,stdin);

    if (strlen(s1)<strlen(s2))
    {
        if (strlen(s2)<strlen(s3))
        {
            printf("max : %s",s3);
        }
        else
        {
            printf("max : %s",s2);
        }
    }
    
    else
    {
        if (strlen(s1)<strlen(s3))
        {
            printf("max : %s",s3);
        }
        else
        {
            printf("max : %s",s1);
        }
    }
    return 0;
}