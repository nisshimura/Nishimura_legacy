#include <stdio.h>
int main()
{   
    int i,a[5];
    printf("input an integer:");
    scanf("%d\n", &a[4]);
    scanf("%d\n", &a[3]);
    scanf("%d\n", &a[2]);
    scanf("%d\n", &a[1]);
    scanf("%d\n", &a[0]);
    for (i=0;i<5;i++) {
        printf("%d",a[i]);
    }
    return 0;
}