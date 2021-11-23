#include <stdio.h>
int main()
{   
    int x,y,i,index,a[9]={0};
    for (i=0;;i++) {
        scanf("%d",&y);
        if (0>y||y>10) {
            printf("Illegal input %d",y);
        }else if (y==0) {
            for (index=0;index<9;index++) {
                printf("[%d]:%d\n",index+1,a[index]);
            }
            return 0;
        }else{
            a[y-1]=a[y-1]+1;
        }
        }
    
    return 0;
}