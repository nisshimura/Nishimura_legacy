#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LINE 256

double my_average(double x)
{
    static double ave,count=1;
    ave  = (x + ave*(count-1))/count;
    count++;
    return ave;
}
int main()
{
    printf("%f\n", my_average(3.3));
    printf("%f\n", my_average(4.4));
    printf("%f\n", my_average(5.5));
    printf("%f\n", my_average(6.6));
    return 0;
}