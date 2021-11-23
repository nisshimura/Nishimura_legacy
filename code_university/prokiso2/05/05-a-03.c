#include <stdio.h>
#include <math.h>

struct point
{
    float x_axis;
    float y_axis;
};

int main()
{
    printf("char         %d(byte)\n",sizeof(char));
    printf("short int    %d(byte)\n",sizeof(short int));
    printf("int          %d(byte)\n",sizeof(int));
    printf("long int     %d(byte)\n",sizeof(long int));
    printf("float        %d(byte)\n",sizeof(float));
    printf("double       %d(byte)\n",sizeof(double));
    printf("struct point %d(byte)\n",sizeof(struct point));
    return 0;
}