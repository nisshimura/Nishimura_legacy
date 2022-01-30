#include <stdio.h>
#include <stdlib.h>
int syracuse(int target, int tesu) {
    if (target == 1) {
        return tesu;
    }
    if (target % 2 == 1) {
        target = target * 3 + 1;
        ++tesu;
    } else {
        target = target / 2;
    }
    syracuse(target, tesu);
}

int main() {
    float **array;
    int i, j, m;
    double n;
    n = 56000, m = 3;

    array = (float **)malloc(sizeof(float *) * n);
    if (array == NULL) {
        printf("out of memory\n");
        exit(1);
    }

    for (i = 0; i < n; i++) {
        array[i] = (float *)malloc(sizeof(float *) * m);
        if (array[i] == NULL) {
            printf("out of memory\n");
            exit(1);
        }
    }
    for (i = 0; i < n; i++) {
        int input = 2 * (i + 1) - 1;
        array[i][0] = (float)input;
        int tesu = syracuse(input, 1);
        array[i][1] = (float)tesu;
        array[i][2] = (float)tesu/(float) input;
    }

    printf("Origin_array\n");

    for (j = 0; j < i; j++) {
        if (j < 20) {
            printf("(%d,%d,%f)\n", (int)array[j][0], (int)array[j][1],
                   array[j][2]);
        }
    }
    printf(".\n.\n.\n");

    for (j = 0; j < i; j++) {
        if (j > n - 4) {
            printf("(%d,%d,%f)\n", (int)array[j][0], (int)array[j][1],
                   array[j][2]);
        }
    }

    free(array);
    return 0;
}