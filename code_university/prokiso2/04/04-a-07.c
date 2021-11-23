#include <stdio.h>
void swap(float *x, float *y)
{
    float z;
    z = *x;
    *x = *y;
    *y = z;
    printf("Swapped 1st:%f,2nd:%f",*x,*y);
}
int main()
{
    float a, b;
    printf("input 1st number :");
    scanf("%f", &a);
    printf("input 1st number :");
    scanf("%f", &b);
    swap(&a,&b);
    return 0;
}