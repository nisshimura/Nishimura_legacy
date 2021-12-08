#include <stdio.h>
#include <math.h>

struct mydate
{
    int y;
    int m;
};

int uru(struct mydate pb)
{
    switch (pb.m)
    {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        return 31;
    case 2:
        if (pb.y%4==0)
            if (pb.y%100==0 && pb.y%400!=0)
            {
                return 28;
            }
            else
            {
                return 29;
            }
        else
        {
            return 28;
        }

    case 4:
    case 6:
    case 9:
    case 11:
        return 30;
    default:
        break;
    }
    }
int main()
{
    struct mydate pa;
    int result;
    printf("input year,month:");
    scanf("%d %d", &(pa.y), &(pa.m));
    result = uru(pa);
    switch (result)
    {
    case 31:
        printf("This month has thirty-one days");
        break;
    case 28:
        printf("This month has twenty-eight days");
        break;
    case 30:
        printf("This month has thirty days");
        break;
    case 29:
        printf("This month has twenty-nine days");
        break;
    default:
        break;
    }
    return 0;
}