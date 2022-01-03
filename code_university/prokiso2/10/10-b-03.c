#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LEN 256

int mystrcat(char *s2,char *s1)
{
    int i=0,len=0;
    len = strlen(s2);
    printf("len:%d\n", len);
    while (s1[i]!='\0')
    {
        s2[len+i] = s1[i];
        //printf("%d", len+i);
        i++;
    }

    return 0;
}
void strrpt(char *s2,char *s1,int n)
{
    int i = 0, len = 0;
    while (s1[i] != '\0')
    {
        s2[len + i] = s1[i];
        // printf("%d", len+i);
        i++;
    }
    s2[len+i] = '\0';
    for (i=0;i<n-1;i++)
    {
        mystrcat(s2,s1);
    }

}
int main()
{
    char s1[100], s2[100];
    int n,len;
    printf("Input string : ");
    fgets(s1,80,stdin);

    len = strlen(s1);
    s1[len - 1] = '\0';

    printf("Input repeat time : ");
    scanf("%d",&n);
    
    strrpt(s2,s1,n);
    printf("[ORG]:%s\n", s1);
    printf("[RPT]:%s", s2);
    return 0;
}