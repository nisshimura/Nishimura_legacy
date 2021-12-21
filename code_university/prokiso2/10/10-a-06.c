#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LINE 256

int mystrlen(char *s)
{
    int i,count=0;
    for (i=0;s[i]!='\0';i++);
    return i;
}
int main()
{
    char s1[MAX_LINE];
    int len1,len2;
    fgets(s1,MAX_LINE,stdin);
    len1 = strlen(s1);
    len2 = mystrlen(s1);
    printf("Length (strlen):%d\n",len1);
    printf("Length (mystrlen):%d",len2);
    return 0;
}
