#include <stdio.h>
int main()
{   
    int x,y,i;
    printf("input an integer:");
    scanf("%d", &x);
    y = x;
    for (i=0;x>=1;i++) {
        if (!(i==0)) {
            x /= 10;
        }
    }
    printf("%d is a %d digits number",y,i-1);
    return 0;
}