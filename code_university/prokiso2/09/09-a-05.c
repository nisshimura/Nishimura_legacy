#include <stdio.h>

void disp_array(int k[][4])
{
    int i,j;
    for (i=0;i<3;i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("%d ",k[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    int array[3][4]={{11,12,13,14},{15,16,17,18},{19,20,21,22}};

    disp_array(array);
    return 0;
}