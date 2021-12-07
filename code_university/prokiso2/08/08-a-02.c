#include <stdio.h>
#include <math.h>

struct mydate
{
    int y;
    int m;
};

struct mydate uru(struct mydate pb)
{
    struct mydate pc = {pb.y, pb.m};
    switch (pb.m)
    {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
        if (pb.d == 31)
        {
            pc.tm++;
            pc.td = 1;
        }
        else
        {
            pc.td++;
        }
        break;
    case 2:
        if (pb.y % 4 == 0 && pb.d == 28)
        {
            pc.td++;
        }
        else if (pb.d >= 28)
        {
            pc.tm++;
            pc.td = 1;
        }
        else
        {
            pc.td++;
        }
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        if (pb.d == 30)
        {
            pc.tm++;
            pc.td = 1;
        }
        else
        {
            pc.td++;
        }
        break;
    case 12:
        if (pb.d == 31)
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
    scanf("%d %d %d", &(pa.y), &(pa.m));
    printdate(pa);
    pc = tomorrow(pa);
    return 0;
}