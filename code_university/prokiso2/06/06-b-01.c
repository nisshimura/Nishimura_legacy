#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next;
    struct number* prev;
    int data;
    };

int d;

struct number head;

void insert(struct number* p,struct number* w)
{
    w->next = p;
    w->prev = p->prev;

    p->prev->next = w;
    p->prev = w;
}
struct number*insert_pos(struct number* p,struct number* w)
{   
    p = p->next;
    while (p!=&head)
    {
        if (p->data>=w->data)
        {
            return p;
        }
        p = p->next;
    }
    return &head;
}
void printasc(struct number* p)
{
    p = p->next;
    while(p!=&head)
    {
        printf("%d",p->data);
        p = p->next;
    }
    printf("\n");
}
void printdsc(struct number* p)
{
    p = p->prev;
    while(p!=&head)
    {
        printf("%d",p->data);
        p = p->prev;
    }
    printf("\n");
}
int main()
{
    head.next = &head;
    head.prev = &head;

    printf("input numbers:\n");

    struct number* p,* q;

    for (;scanf("%d",&d)!=EOF;)
    {   
        p=(struct number *)malloc(sizeof(struct number));
        p->data=d;
        q = insert_pos(&head,p);
        insert(q,p);
    }
    printasc(&head);
    printdsc(&head);
    return 0;
}