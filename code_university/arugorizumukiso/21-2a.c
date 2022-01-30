#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number *next;
    struct number *prev;
    int data;
    int chainlength;
    float divchain;
};

int d;

struct number head;
void add_list(struct number *input)
{
    struct number *p;
    p = (struct number *)malloc(sizeof(struct number));
    if (p == NULL)
    {
        printf("out of memory\n");
        exit(1);
    }

    if (head.next == &head)
    {
        p = input;
        head.next = p;
        head.prev = p;

        p->next = &head;
        p->prev = &head;
    }
    else
    {
        p = input;
        p->next = &head;
        p->prev = head.prev;
        head.prev = p;
    }
}
void insert(struct number *p, struct number *w)
{
    w->next = p;
    w->prev = p->prev;

    p->prev->next = w;
    p->prev = w;
}
struct number *insert_pos(struct number *p, struct number *w)
{
    p = p->next;
    while (p != &head)
    {
        if (p->data >= w->data)
        {
            return p;
        }
        p = p->next;
    }
    return &head;
}
void printasc(struct number *p)
{
    p = p->next;
    while (p != &head)
    {
        printf("%d", p->data);
        p = p->next;
    }
    printf("\n");
}
void printdsc(struct number *p)
{
    p = p->prev;
    while (p != &head)
    {
        printf("%d", p->data);
        p = p->prev;
    }
    printf("\n");
}

int syracuse(int target, int tesu)
{
    if (target == 1)
    {
        return tesu;
    }
    if (target % 2 == 1)
    {
        target = target * 3 + 1;
        syracuse(target, ++tesu);
    }
    else
    {
        while (target % 2 != 1)
        {
            target = target / 2;
        }
        syracuse(target, tesu);
    }
}

int main()
{
    head.next = &head;
    head.prev = &head;

    struct number *p;

    for (int i=1;;i++)
    {
        p = (struct number *)malloc(sizeof(struct number));
        if (p == NULL)
        {
            printf("out of memory\n");
            break;
        }
        p->data = 2 * i - 1;
        int tesu = syracuse(p->data,0);
        p->chainlength = tesu;
        p->divchain = (float)p->chainlength/(float)tesu;
        add_list(p);
    }

    
    return 0;
}