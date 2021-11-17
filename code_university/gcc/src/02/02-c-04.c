#include <stdio.h>
int main()
{
    int i,th,hun,ten,one;
    printf("Input an integer:");
    scanf("%d",&i);
    if (i==0){
        printf("0=0");
        return 0;
    }else if (0>i || i>10000){
        printf("Incorrect input.");
        return 0;
    }

    th = i/1000;
    hun = (i - th*1000)/100;
    ten = (i-th*1000-hun*100)/10;
    one = i%10;

    if (ten<1){
        printf("%d = %d",i,one);
    }else if (hun<1){
        printf("%d = %d x 10 + %d",i,ten,one);
    }else if (th<1){
        printf("%d = %d x 100 + %d x 10 + %d",i,hun,ten,one);
    }else{
        printf("%d = %d x 1000 + %d x 100 + %d x 10 + %d",i,th,hun,ten,one);
    }
    return 0;
}