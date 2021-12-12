#include <stdio.h>

int a[3][3], b[3][3], c[3][3];

void print_arr3x3(int a[][3])
{
    int i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}
void get_arr3x3(int a[][3])
{
    int i, j;
    scanf("%d %d %d %d %d %d %d %d %d", &a[0][0], &a[0][1], &a[0][2], &a[1][0], &a[1][1], &a[1][2], &a[2][0], &a[2][1], &a[2][2]);
}
void sum_arr3x3(int a[][3], int b[][3], int c[][3])
{
    int i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}
int main()
{
    get_arr3x3(a);
    printf("a\n");
    print_arr3x3(a);
    get_arr3x3(b);
    printf("b\n");
    print_arr3x3(b);
    printf("a+b\n");
    sum_arr3x3(a,b,c);
    print_arr3x3(c);
}