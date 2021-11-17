#include <stdio.h>
int main()
{
    int i,j,k,l;
    printf("after time h1:m1\n");
    printf("input h1 m1:");
    scanf("%d %d", &i, &j);
    printf("before time h1:m1\n");
    printf("input h1 m1:");
    scanf("%d %d", &k, &l);
    
    printf("%d %d\n",i - k,j - l);
    printf("%d",(i-k)*60+(j-l));
    
    return 0;
}