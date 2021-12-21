#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LEN 256

int mystrcat(char *s1,char *s2)
{
    int i=0,len;
    len = strlen(s1);
    printf("%d",len);
    while (s2[i]!='\0')
    {
        if (s2[i]=='\n')
        {
            ;
        }
        else
        {
            s1[len + i] = s2[i];
        }
        i++;
    }
    return 0;
}
void strrpt(char *s1,char *s2,int n)
{
    int i;
    for (i=0;i<n;i++)
    {
        mystrcat(s1,s2);
    }
}
int main()
{
    char s1[MAX_LEN], s2[MAX_LEN];
    int n,len;
    printf("Input string : ");
    fgets(s1,MAX_LEN,stdin);
    len = strlen(s1);
    printf("%d", len);
    s1[len-1] = '\0';
    len = strlen(s1);
    printf("%d",len);
    printf("Input repeat time : ");
    scanf("%d",&n);

    strrpt(s2,s1,n);

    printf("[ORG]:%s\n", s1);
    printf("[RPT]:%s", s2);
    return 0;
}