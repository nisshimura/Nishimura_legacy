#include <stdio.h>
int main()
{   
    int x,i,result;
    printf("input an integer:");
    scanf("%d", &x);
    result = 1;
    for (i=0;i<=x;i++) {
        if (!(i==0)) {
            result *= i;
        }
    }
    printf("%d! = %d",i,result);
    return 0;
}