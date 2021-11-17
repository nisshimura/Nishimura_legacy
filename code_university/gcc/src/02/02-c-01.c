#include <stdio.h>
#include <math.h>
int main()
{
    float i,j,k,l,ave,dis;
    printf("Input 1st number:");
    scanf("%f",&i);
    printf("Input 2nd number:");
    scanf("%f",&j);
    printf("Input 3rd number:");
    scanf("%f",&k);
    printf("Input 4th number:");
    scanf("%f",&l);
    
    ave = (i+j+k+l)/4;
    dis = (pow(i-ave,2.0)+pow(j-ave,2.0)+pow(k-ave,2.0)+pow(l-ave,2.0))/4;
    
    printf("Average:%f\n",ave);
    printf("Dispersion:%f",dis);

    return 0;
}