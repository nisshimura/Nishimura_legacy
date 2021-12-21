#include <stdio.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    char s1[MAX_LINE];
    int key,i;
    printf("input string : ");
    fgets(s1,MAX_LINE,stdin);
    printf("input key : ");
    scanf("%d",&key);
    for (i=0;i<strlen(s1);i++)
    {
        s1[i]=s1[i]+key;
    }
    printf("%s",s1);
    return 0;
}