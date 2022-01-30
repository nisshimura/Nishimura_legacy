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
int sosu(int now, float **array) {
    int i, j;
    int sosu[2];

    int flag;

    for (i = now;; i++) {
        flag = 0;

        for (j = 0; array[j][0] != 0; j++) {
            if (i % (int)array[j][0] == 0) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            return i;
        }
    }
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
    float **array, *tmparray;
    int i, j, n, m;
    int now, input = 2;
    n = 1000, m = 3;

    array = calloc(n, sizeof(float *));
    if (array == NULL) {
        printf("out of memory\n");
        exit(1);
    }
    tmparray = calloc(n * m, sizeof(float));
    if (tmparray == NULL) {
        printf("out of memory\n");
        exit(1);
    }

    for (i = 0; i < n; i++) {
        array[i] = tmparray + i * m;
    }

    for (i = 0; i < n; i++) {
        // input = 2 * (i + 1) - 1;
        input = sosu(input, array);
        array[i][0] = (float)input;
        int tesu = syracuse(input, 1);
        array[i][1] = (float)tesu;
        array[i][2] = (float)input / (float)tesu;
    }
    clock_t start_clock, end_clock;

    start_clock = clock();

    quick_sort(array, 0, i - 1);
    end_clock = clock();

    printf("Sosu_array\n");

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
    free(tmparray);
    free(array);

    return 0;
}