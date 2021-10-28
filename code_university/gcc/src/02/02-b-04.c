#include <stdio.h>
int main()
{
    int i;
    printf("input number:");
    scanf("%d",&i);

    if (i==0){
        printf("Input number is 0.");
        return 0;
    }

    printf("%d is...\n", i);

    float amari = i % 2;
    if (amari==0){
        printf("Positive even number.");
    }
    else{
        printf("Negative even number.");
    }
    
    return 0;
}