#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct calc_result
{
    float wa;
    float sa;
    float seki;
    float syo;
};

struct calc_result* get_calc_result(float a ,float b)
{
    struct calc_result *p;
    p = (struct calc_result *)malloc(sizeof(struct calc_result));
    p->wa = a + b;
    p->sa = a - b;
    p->seki = a * b;
    if (b==0){
        p->syo = 0;
    }
    else{
        p->syo = a / b;
    }
    return p;
}    

int main()
{   
    struct calc_result *q;
    q = (struct calc_result *)malloc(sizeof(struct calc_result));
    float a,b;
    printf("Input two integers:");
    scanf("%f %f",&a,&b);
    q = get_calc_result(a,b);
    printf("%f + %f = %f\n",a,b,q->wa);
    printf("%f - %f = %f\n",a,b,q->sa);
    printf("%f * %f = %f\n",a,b,q->seki);
    printf("%f / %f = %f\n",a,b,q->syo);
    return 0;
}