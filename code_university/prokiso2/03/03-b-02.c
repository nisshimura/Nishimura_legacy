#include <stdio.h>
int main()
{   
    int x,index,i,a[32]={0};
    printf("input decimal number:");
    scanf("%d",&x);

    for (index=0;x>=1;index++) {
        a[index] = x%2;
        x = x / 2;
    }

    printf("binary number:");

    for (i=0;i<index;i++) {

        printf("%d",a[index-i-1]);
    }
    return 0;
}