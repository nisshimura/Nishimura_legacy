#include <stdio.h>

int i=1;
void print_sequence(int n)
{
    if (i>n)
    {
        return;
    }
    printf("%d",i++);
    print_sequence(n);
}
int main()
{
    int k;
    printf("input an integer");
    scanf("%d",&k);
    print_sequence(k);
    return 0;
}