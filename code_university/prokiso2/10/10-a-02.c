#include <stdio.h>
#include <string.h>
#define MAX_LINE 256

int main()
{
    char line[MAX_LINE],output[MAX_LINE];
    fgets(line,MAX_LINE,stdin);
    strncpy(output,line,3);
    printf("%s",output);
    return 0;
}