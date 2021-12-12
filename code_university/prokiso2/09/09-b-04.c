#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number *next;
    struct number *prev;
    char data;
    int ascii;
    
};

char d;

struct number head;

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
        if (p->ascii >= w->ascii)
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
        printf("%c", p->data);
        p = p->next;
    }
    printf("\n");
}

int main()
{
    head.next = &head;
    head.prev = &head;



    struct number *p, *q;

    do
    {
        d = getchar();
        if (d >= '0' && d <= '9')
        {
            break;
        }
        p = (struct number *)malloc(sizeof(struct number));
        p->data = d;
        int k = d;
        p->ascii = k;
        q = insert_pos(&head, p);
        insert(q, p);
    }
    while (1);

    printasc(&head);
    return 0;
}