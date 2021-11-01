#include <stdio.h>
int main()
{
    int one,two,three,temp;
    printf("input 1:");
    scanf("%d",&one);
    printf("input 2:");
    scanf("%d",&two);
    printf("input 3:");
    scanf("%d",&three);

    if (one >= two){
        temp = one;
        one = two;
        two = temp;
    }else{
        ;
    }
    if (one >= three){
        temp = one;
        one = three;
        three = temp;
    }else{
        ;
    } 
    if (two >= three){
        temp = two;
        two = three;
        three = temp;
    }else{
        ;
    }
    printf("Sorted:%d,%d,%d",one,two,three);
    return 0;
}