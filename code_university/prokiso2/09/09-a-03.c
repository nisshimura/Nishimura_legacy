#include <stdio.h>

void init_array(float f[],int k)
{   
    int i;
    for (i=0;i<k;i++)
    {
        f[i]=0.0;
        printf("f[%d]:%f\n", i,f[i]);
    }
}
int main()
{
    float f[10];
    init_array(f,10);
}