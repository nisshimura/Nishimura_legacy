#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

//Windows10上でコマンドラインから入力しました
// 11-a-05.exe 12.3 45.6
//出力
// 12.3 + 45.6 = 57.900000
// 12.3 - 45.6 = -33.300000
// 12.3 * 45.6 = 560.880000
// 12.3 / 45.6 = 0.269737

int main(int argc,char *argv[])
{
    if (argc>3)
    {
        printf("Error");
        exit(1);
    }

    int num, chr, len;

    printf("%s + %s = %lf\n", argv[1], argv[2], atof(argv[1]) + atof(argv[2]));
    printf("%s - %s = %lf\n", argv[1], argv[2], atof(argv[1]) - atof(argv[2]));
    printf("%s * %s = %lf\n", argv[1], argv[2], atof(argv[1]) * atof(argv[2]));
    printf("%s / %s = %lf\n", argv[1], argv[2], atof(argv[1]) / atof(argv[2]));
    return 0;
}