#include <stdio.h>
#include <math.h>

struct point
{
    float x_axis;
    float y_axis;
};

int main()
{
    float tilt,intercept;
    struct point pa,pb;

    printf("Input first point (x1,y1):");
    scanf("%f %f",&(pa.x_axis),&(pa.y_axis));

    printf("Input first point (x2,y2):");
    scanf("%f %f",&(pb.x_axis),&(pb.y_axis));

    tilt = (pa.y_axis-pb.y_axis)/(pa.x_axis-pb.x_axis);
    intercept = pa.y_axis-tilt*pa.x_axis;
    
    printf("linear functino: y=%fx+%f",tilt,intercept);
    return 0;
}