#include <stdio.h>
int main()
{
    int i,*ip;
    char c='0',*cp;
    
    ip = &i;
    cp = &c;
    printf("ip:    %p\n",ip);
    ++i;
    ip = &i;
    printf("++ip : %p\n",ip);
    printf("cp :   %p\n",cp);
    ++c;
    cp = &c;
    printf("++cp : %p\n",cp);
    return 0;
}