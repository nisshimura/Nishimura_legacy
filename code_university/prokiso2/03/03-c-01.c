#include <stdio.h>
int main()
{   
    int x,i,index,j,k,a[20][20]={0};
    printf("input number:");
    scanf("%d", &x);
    for (i=0;i<x;i++) {
        for (index=0;index<=i;index++) {
            if (index==0||index==x-1) {
                a[i][index] = 1;
            }else{
                a[i][index] = a[i-1][index] + a[i-1][index-1];
            }
        }
    }
    for (j=x;j>0;j--) {
        printf("\n");
        for (k=0;k<=j-1;k++) {
            printf(" %d ",a[j-1][k]);
        }
    }
    return 0;
}