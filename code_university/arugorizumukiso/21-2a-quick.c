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

void quick_sort(float **input, int left, int right) {
    int i, j;
    float pivot, *temp;

    i = left;
    j = right;
    pivot = input[(left + right) / 2][2];
    while (1) {
        while (input[i][2] < pivot) {
            i++;
        }
        while (pivot < input[j][2]) {
            j--;
        }
        if (i >= j) {
            break;
        }
        temp = input[i];
        input[i] = input[j];
        input[j] = temp;

        i++;
        j--;
    }

    if (left < i - 1) {
        quick_sort(input, left, i - 1);
    }
    if (j + 1 < right) {
        quick_sort(input, j + 1, right);
    }
}

int main() {
    float **array;
    int i, j, n, m;
    int input;
    n = 5000, m = 3;

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
        array[i][2] = (float)tesu / (float)input;
    }

    clock_t start_clock, end_clock;

    start_clock = clock();

    quick_sort(array, 0, i - 1);
    end_clock = clock();

    printf("Quicked_array\n");

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

    free(array);
    printf(
        "\n-------------------\nQuicked_array:clock=%f\n-------------------\n",
        (double)(end_clock - start_clock) / CLOCKS_PER_SEC);
    return 0;
}