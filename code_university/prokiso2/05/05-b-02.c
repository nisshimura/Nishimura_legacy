#include <stdio.h>
#include <math.h>

struct mydate
{
    int y;
    int m;
    int d;
};
struct date
{
    int ty;
    int tm;
    int td; 
};

void printdate(struct mydate pa)
{

    printf("Today is %04d/%02d/%02d\n",pa.y,pa.m,pa.d);

}
struct date tomorrow(struct mydate pb)
{
    struct date pc={pb.y,pb.m,pb.d};
    switch (pb.m)
    {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
        if (pb.d==31)
        {
            pc.tm++;
            pc.td=1;
        }else{
            pc.td++;
        }
        break;
    case 2:
        if (pb.y%4==0&&pb.d==28)
        {
            pc.td++;
        }else if(pb.d>=28)
        {
            pc.tm++;
            pc.td=1;
        }else
        {
            pc.td++;
        }
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        if (pb.d==30)
        {
            pc.tm++;
            pc.td=1;
        }else{
            pc.td++;
        }
        break;
    case 12:
        if (pb.d==31)
        {
            pc.ty++;
            pc.tm = 1;
            pc.td = 1;
        }
    
    default:
        break;
    }
    return pc;
}
int main()
{
    struct mydate pa;
    struct date pc;
    
    scanf("%d %d %d",&(pa.y),&(pa.m),&(pa.d));
    printdate(pa);
    pc = tomorrow(pa);
    printf("Tomorrow is %04d/%02d/%02d",pc.ty,pc.tm,pc.td);
    return 0;
}