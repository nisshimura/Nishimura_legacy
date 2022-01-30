#include <stdio.h>
#include <stdlib.h>
#define MAXLINE 256

struct zyun
{
    struct zyun *next;
    int s[MAXLINE];
};

struct zyun *head;
struct zyun *tail;

void add_list(struct zyun input)
{
    struct zyun *p;
    p = (struct zyun *)malloc(sizeof(struct zyun));
    if (p == NULL)
    {
        printf("out of memory\n");
        exit(1);
    }
    if (tail == NULL)

    {
        head = p;
    }
    else
    {
        tail->next = p;
    }
    tail = p;
    *tail = input;
    tail->next = NULL;
}

void print_head(int n)
{
    struct zyun *p;

    p = head;
    while (p != NULL)

    {
        int i;
        for (i = 0; i < n; i++)

        {
            printf(" %d", p->s[i]);
        }
        printf("\n");
        p = p->next;
    }
}

int get_zyunretsu(int *arr, int n)
{
    int left = n - 2;
    while (left >= 0 && arr[left] >= arr[left + 1])

    {
        left--;
    }

    if (left < 0)

    {
        return 0;
    }

    int right = n - 1;

    while (arr[left] >= arr[right])

    {
        right--;
    }

    int t = arr[left];
    arr[left] = arr[right];
    arr[right] = t;

    left++;
    right = n - 1;

    while (left < right)

    {
        int t = arr[left];
        arr[left] = arr[right];
        arr[right] = t;

        left++;
        right--;
    }

    return 1;
}

int main()
{
    int n, i;
    struct zyun *x;

    printf("Input n : ");
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++)
        arr[i] = (i + 1);
    do
    {
        x = (struct zyun *)malloc(sizeof(struct zyun));
        for (int i = 0; i < n; i++)

        {
            x->s[i] = arr[i];
        }
        add_list(*x);

    } while (get_zyunretsu(arr, n));

    print_head(n);

    return 0;
}
