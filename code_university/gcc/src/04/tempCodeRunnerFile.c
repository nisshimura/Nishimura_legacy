#include <stdio.h>
int aster(int x)
{  
    int i;

    for (i=0;i<x;i++) {
        printf("*");
    }
    return 0;
}
int main()
{   
    int z;
    printf("input a positive integer:");
    scanf("%d", &z);
    int y = aster(z);
}