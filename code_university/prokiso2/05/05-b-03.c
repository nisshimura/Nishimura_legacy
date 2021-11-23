#include <stdio.h>
#include <math.h>

struct point
{
    float x_axis;
    float y_axis;
};

struct circle
{
    struct point p;
    float r;
};

int circle_intersect(struct circle pc,struct circle pd)
{
    float d;
    d = sqrt(pow(pc.p.x_axis-pd.p.x_axis,2.0) + pow(pc.p.y_axis-pd.p.y_axis,2.0));
    if (pc.r>=pd.r)
    {
        if (pc.r-pd.r<d && d<pc.r+pd.r)
        {
            return 2;
        }
        else if ((pc.r+pd.r)==d)
        {
            return 1;
        }
        else
        {
            return 0;
        }
        
    }
    else if (pc.r<pd.r)
    {
        if (pd.r-pc.r<d && d<pd.r+pc.r)
        {
            return 2;
        }
        else if ((pc.r+pd.r)==d)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}
int main()
{
    struct point pa,pb;
    struct circle pc,pd;
    int result;

    printf("Input 1st Circle (x,y,r):");
    scanf("%f %f %f",&(pc.p.x_axis),&(pc.p.y_axis),&(pc.r));

    printf("Input 2nd Circle (x,y,r):");
    scanf("%f %f %f",&(pd.p.x_axis),&(pd.p.y_axis),&(pd.r));

    result = circle_intersect(pc,pd);
    printf("Circles have %d intersect point",result);
    
    return 0;
}