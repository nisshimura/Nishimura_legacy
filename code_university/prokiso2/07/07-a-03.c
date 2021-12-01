#include <stdio.h>

int i=0;

int tousa(int a ,int d,int n)
{
    if (i==n)
    {
        return 0;
    }
    printf("[%d]:%d\n",++i,a);
    tousa(a+d,d,n);
}
int main()
{
    int a,b,c;
    printf("input a d n:");
    scanf("%d %d %d",&a,&b,&c);
    tousa(a,b,c);
    return 0;
}