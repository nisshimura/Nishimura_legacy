#include <stdio.h>
float calc(float a,float b,char c) {  
    float result;
    // if (c="+") {
    //     result = a + b;
    // }else if (c=="-") {
    //     result = a - b;
    // }else if (c=="*") {
    //     result = a * b;
    // }else if (c=="/") {
    //     if (a==0 || b==0){
    //         return 0;
    //     }
    //     result = a / b;
    // }
    result  = a 
    return result;
}

int main(void){
float a = 1234, b = 5678;
printf("%f + %f = %f\n", a, b, calc(a, b, '+'));
printf("%f - %f = %f\n", a, b, calc(a, b, '-'));
printf("%f * %f = %f\n", a, b, calc(a, b, '*'));
printf("%f / %f = %f\n", a, b, calc(a, b, '/'));
return 0;
}
