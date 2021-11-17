#include <stdio.h>
int main()
{   
    int x,y,i,index,max,min,sum,a[30];
    printf("input array size:");
    scanf("%d",&x);
    printf("input array element:");

    max = 0;
    min = 0;
    sum = 0;

    for (i=0;i<x;i++) {
        scanf("%d",&y);
        a[i] = y;
        }
    for (index=0;index<i;index++) {
        sum += a[index];
        if (index==0) {
            min = a[index];
            max = a[index];
        }
        if (a[index]>max) {
            max = a[index];
        }
        if (a[index]<min) {
            min = a[index];
        }

    }
    float average = (float)sum / (float)i;
    printf("max:%d,min:%d,average:%f",max,min,average);
    return 0;
}