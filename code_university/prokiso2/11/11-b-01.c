#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    FILE *fp1, *fp2;
    char file1[MAX_LINE], file2[MAX_LINE];
    int chr1,chr2,count,current=0,len;

    printf("File1 : ");
    fgets(file1, MAX_LINE, stdin);

    len = strlen(file1);
    file1[len - 1] = '\0';

    printf("File2 : ");
    fgets(file2, MAX_LINE, stdin);

    len = strlen(file2);
    file2[len - 1] = '\0';

    fp1 = fopen(file1, "r");
    fp2 = fopen(file2, "r");

    if (fp1 == NULL || fp2 == NULL)
    {
        printf("open error.");
        exit(1);
    }

    while ((chr1 = fgetc(fp1)) != EOF)
    {
        count = 0;
        if ((chr1 >= 'a' && chr1 <= 'z') || (chr1 >= 'A' && chr1 <= 'Z'))

        {
            while ((chr2 = fgetc(fp2)) != EOF)
            {
                if ((chr2 >= 'a' && chr2 <= 'z') || (chr2 >= 'A' && chr2 <= 'Z'))

                {
                    if (chr1 == chr2)
                    {
                        break;
                    }
                    else
                    {
                        printf("NotEqual");
                        exit(1);
                    }
                }
            }
        }
    }
    printf("Equal");

    fclose(fp1);
    fclose(fp2);

    return 0;
}