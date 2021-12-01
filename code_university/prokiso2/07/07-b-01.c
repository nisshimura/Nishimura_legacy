#include <stdio.h>

int i=0;
float ruizyo=1;

float my_pow(int a ,int b)
{
    if (i==b|i==-b)
    {
        return ruizyo;
    }
    ++i;
    if (b<0)
    {
        ruizyo/=a;
    }
    else
    {
        ruizyo*=a;
    }
    my_pow(a,b);
}
int main()
{
    int a,b,c;
    printf("input two integers:");
    scanf("%d %d",&a,&b);
    printf("a^b=%f",my_pow(a,b));
    return 0;
}