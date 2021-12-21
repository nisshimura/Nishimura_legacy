#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LEN 256

int mystrrev(char *s1,char *s2)
{
    int i=0,len;
    len = strlen(s2)-1;
    while (s2[i]!='\0')
    {
        if (s2[len-i]=='\n')
        {
            ;
        }
        else
        {
            s1[i]=s2[len-i];
        }
        i++;
    }
    return 0;
}
int main()
{
    char s1[MAX_LEN], s2[MAX_LEN];
    fgets(s2,MAX_LEN,stdin);
    mystrrev(s1, s2);

    printf("[IN]%s", s2);
    printf("[REV]%s", s1);
    return 0;
}