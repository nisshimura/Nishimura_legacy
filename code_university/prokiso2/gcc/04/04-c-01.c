#include <stdio.h>
int main()
{
    char index,a;
    int i;
    printf("Input shift num:");
    scanf("%c",&index);
    int num = index - '0'; 
    char data[10];

    printf("Input text:");
    for (i=0;;i++)
    {
        scanf("%c",&a);
        if (a=='\n'){
            break;
        }
        data[i] = a;
    }
    
    for (i=0;i<=10;i++){
        printf("%c",data[i]);
    }

}