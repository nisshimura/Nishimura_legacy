#include <stdio.h>
int main()
{   
    int x,index,sum;
    printf("Please input number:");
    scanf("%d",&x);
    if (1>x || x>100) {
        printf("Error:input range is 1 to 100");
        return 0;
    }
    sum = 0;
    for (index=0;index<=x;index++) {
        sum += index;
    }

    printf("Sum 1-%d is %d",x,sum);
    return 0;
}