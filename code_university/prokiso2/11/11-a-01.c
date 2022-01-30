#include <stdio.h>
#include <stdlib.h>
#define MAX_LINE 256

int main()
{
    FILE *fp;
    char s1[MAX_LINE];
    int num;

    printf("Input name : ");
    fgets(s1, MAX_LINE, stdin);

    printf("Input student number : ");
    scanf("%d", &num);

    fp = fopen("11-a-01.txt","w");

    if (fp==NULL)
    {
        printf("open error.");
        exit(1);
    }

    fprintf(fp,"ID=%d,name=%s",num,s1);
    fclose(fp);

    return 0;
}