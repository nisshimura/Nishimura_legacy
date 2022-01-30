#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    FILE *fp ,*fp_out;
    char input[MAX_LINE], output[MAX_LINE];
    int num,chr,len;

    printf("Input filename : ");
    fgets(input, MAX_LINE, stdin);

    
    len = strlen(input);
    input[len - 1] = '\0';

    printf("Output filename : ");
    fgets(output, MAX_LINE, stdin);

    len = strlen(output);
    output[len - 1] = '\0';

    printf("Loop num : ");
    scanf("%d", &num);

    fp_out = fopen(output, "w");

    for (int i = 0; i < num; i++)
    {
        fp = fopen(input, "r");
        if (fp == NULL)
        {
            printf("open error.");
            exit(1);
        }
        while ((chr = fgetc(fp)) != EOF)
        {
            fprintf(fp_out, "%c",chr);
        }
    }
    fclose(fp);

    return 0;
}