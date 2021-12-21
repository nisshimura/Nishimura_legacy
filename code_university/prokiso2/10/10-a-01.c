#include <stdio.h>
#define MAX_LINE 256

int main()
{
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin);
    printf("%s",line);
    return 0;
}