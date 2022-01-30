#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int syracuse(int target, int tesu) {
    if (target == 1) {
        return tesu;
    }
    if (target % 2 == 1) {
        target = target * 3 + 1;
        tesu++;
    } else {
        target = target / 2;
    }
    syracuse(target, tesu);
}

void buble_sort(float **input, int array_size) {
    int i, j;
    float *temp;

    for (i = 0; i < array_size - 1; i++) {
        for (j = array_size - 1; j > i; j--) {
            if (input[j - 1][2] > input[j][2]) {
                temp = input[j - 1];
                input[j - 1] = input[j];
                input[j] = temp;
            }
        }
    }
}
int main() {
    float **array;
    int i, j, n, m;
    n = 5000, m = 3;

    array = (float **)malloc(sizeof(float *) * n);
    if (array == NULL) {
        printf("out of memory\n");
        exit(1);
    }
    for (i = 0; i < n; i++) {
        array[i] = (float *)malloc(sizeof(float *) * m);
    }

    for (i = 0; i < n; i++) {
        int input = 2 * (i + 1) - 1;
        array[i][0] = (float)input;
        int tesu = syracuse(input, 1);
        array[i][1] = (float)tesu;
        array[i][2] = (float)tesu / (float)input;
    }

    clock_t start_clock, end_clock;

    start_clock = clock();

    buble_sort(array, i);

    end_clock = clock();
    printf("Bubled_array\n");

    for (j = 0; j < i; j++) {
        if (j < 3) {
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

    printf(
        "\n-------------------\nBubled_array:clock=%f\n-------------------\n",
        (double)(end_clock - start_clock) / CLOCKS_PER_SEC);

    free(array);
    return 0;
}