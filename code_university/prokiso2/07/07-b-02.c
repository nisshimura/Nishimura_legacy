#include <stdio.h>

int i=0;
int p=1,c=1;
void my_retsu(int a ,int b)
{
    if (i==b)
    {
        printf("%dP%d=%d\n", a, b, p);
        printf("%dC%d=%d\n", a, b, p/c);
        return;
    }
    p*=a-i;
    c*=b-i;
    ++i;  
    my_retsu(a,b);
}
int main()
{
    int a,b,pans,cans;
    printf("input m and n:");
    scanf("%d %d",&a,&b);
    my_retsu(a,b);

    return 0;
}