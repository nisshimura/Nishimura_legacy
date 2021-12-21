#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LEN 256

int mystrcat(char *s1,char *s2)
{
    int i=0,len;
    len = strlen(s1);
    while (s1[i]!='\0')
    {
        s1[len+i]=s2[i];
        i++;
    }
    return 0;
}
int main()
{
    char str1[MAX_LEN] = "abc", str2[] = "def";
    mystrcat(str1, str2);
    printf("%s", str1);
    return 0;
}