#include <stdio.h>
int main()
{
    char a;
    int i,count=0,sum=0;
    for (i=0;;i++){
        scanf("%c", &a);
        if (a=='E'){
            printf("Sum is:%d\n", sum);
            printf("Average is:%f", (float)sum / (float)count);
            return 0;
        }
        int target = a - '0';
        if (target >= 0 && target <= 9) {
            sum += a - '0';
            count += 1;
        }else if (a=='\n') {
            ;
        }else{
            printf("Illegal input:%c\n",a);
        }
            
    }

}