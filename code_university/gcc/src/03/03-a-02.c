#include <stdio.h>
int main()
{   
    int x,i;
    printf("input an integer:");
    scanf("%d", &x);
    for (i=0;i<x;i++) {
        printf("*");
    }
    return 0;
}