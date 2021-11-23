#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct student_data {
    int num;
    int height;
    int weight;
};

int main()
{
    int a,b,c,i,tallest=0,shortest=0,heaviest=0,lightest=0;
    char d;
    struct student_data list[10];
    for (i=0;i<=10;i++){
        printf("Input student number,height,weight:");
        scanf("%d %d %d",&a,&b,&c);
        scanf("%c",&d);
        if (a < 0){
            break;
        }else{
            if (i==0){
                tallest = i;
                shortest = i;
                heaviest = i;
                lightest = i;
            }else{
                if (list[tallest].height <= b){
                    tallest = i;
                };
                if (list[shortest].height >= b){
                    shortest = i;
                };
                if (list[heaviest].weight <= c){
                    heaviest = i;
                }
                if (list[lightest].weight >= c){
                    lightest = i;
                };   
            };
            list[i].num = a;
            list[i].height = b;
            list[i].weight = c;
        };
    };
    printf("Tallest   student number is %d(%dcm)\n",list[tallest].num,list[tallest].height);
    printf("Shortest  student number is %d(%dcm)\n",list[shortest].num,list[shortest].height);
    printf("Heaviest  student number is %d(%dkg)\n",list[heaviest].num,list[heaviest].weight);
    printf("Lightest  student number is %d(%dkg)\n",list[lightest].num,list[lightest].weight);

    return 0;
}