#include <stdio.h>
int main()
{   
    int index,i,a[5][5];

    for (index=0;index<5;index++) {
        printf("\n");
        for (i=0;i<5;i++) {
            if (index==i) {
                a[index][i] = 1;
            }else {
                a[index][i] = 0;
            }
            printf("%d",a[index][i]);
        }
    }
    return 0;
}