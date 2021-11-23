#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct score {
    int num;
    int math;
    int eng;
    int sci;
};

void print_total_average(struct score *q)
{
    int total;
    float ave;

    total = q->eng+q->math+q->sci;
    ave = (float)total/3;
    printf("student[%d] total:%d,average:%f\n",q->num,total,ave);
}
int main()
{
    int i;
    struct score list[3] = {
        {61500001,90,72,55},
        {61500002,82,77,85},
        {61500003,65,91,73},
    };
    for (i=0;i<3;i++){
        print_total_average(&(list[i]));
    }
    return 0;
}