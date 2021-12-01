#include <stdio.h>

int i=0;
int p=1,c=1;

int my_retsu(int a ,int b)
{
    if (i==b)
    {
        return p,c;
    }
    ++i;
    p*=
    
    a;
    my_retsu(a-1,b);
}
int main()
{
    int a,b;
    printf("input two integers:");
    scanf("%d %d",&a,&b);
    printf("a^b=%d",my_retsu(a,b));
    return 0;
}