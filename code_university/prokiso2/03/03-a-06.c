#include <stdio.h>
int main()
{   
    int i,current,preprenum,prenum;
    current = 0;
    preprenum = 1;
    prenum  = 0;

    for (i=1;i<21;i++) {
        current = prenum + preprenum;
        preprenum = prenum;
        prenum = current;

        printf("fib[%d]:%d\n",i,current);
    }
    return 0;
}