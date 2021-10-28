#include <stdio.h>
int main()
{
    int i;
    printf("input an integer:");
    scanf("%d",&i);

    if ((i%2)==0&&(i%3)==0&&(i%5)==0){
        printf("%d is divisible by 2,3 and 5.",i);
    }else if ((i%2)==0&&(i%3)==0){
        printf("%d is divisible by 2 and 3 but not divisible by 5",i);
    }else if ((i%2)==0&&(i%5)==0){
        printf("%d is divisible by 2 and 5 but not divisible by 3",i);
    }else if ((i%3)==0&&(i%5)==0){
        printf("%d is divisible by 3 and 5 but not divisible by 2",i);
    }else if ((i%2)==0 ){
        printf("%d is divisible by 2 but not divisible by 3 nor 5",i);
    }else if ((i%3)==0){
        printf("%d is divisible by 3 but not divisible by 2 nor 5",i);
    }else if ((i%5)==0){
        printf("%d is divisible by 5 but not divisible by 2 nor 3",i);
    }else{
        printf("%d isn't divisible by 2,3 nor 5",i);
    }

    return 0;
}