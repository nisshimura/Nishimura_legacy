#include <stdio.h>
void mytoupper(char *c){
    char big;
    big = *c - 'a' + 'A';
    printf("Output charcter:%c",big);
}
int main()
{
    char x;
    printf("Input character:%c",x);
    scanf("%c",&x);
    mytoupper(&x);
    return 0;
}