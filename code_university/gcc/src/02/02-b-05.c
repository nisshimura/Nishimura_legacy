#include <stdio.h>
int main()
{
    int i;
    printf("input your score:");
    scanf("%d",&i);

    if (0>i || i>100){
        printf("error:input from 0 to 100");
    }else if (i>=50){
        printf("you passed the examination.");
    }else{
        printf("you failed the examination.");
    }
    return 0;
}