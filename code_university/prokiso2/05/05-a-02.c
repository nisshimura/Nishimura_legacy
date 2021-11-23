#include <stdio.h>
#include <math.h>

struct mydate
{
    int y;
    int m;
    int d;
};

void printdate(struct mydate pa)
{

    printf("%04d/%02d/%02d",pa.y,pa.m,pa.d);

}
int main()
{
    struct mydate pa;
    scanf("%d %d %d",&(pa.y),&(pa.m),&(pa.d));
    printdate(pa);
    return 0;
}