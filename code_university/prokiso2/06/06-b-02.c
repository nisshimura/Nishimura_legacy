#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next;
    struct number* prev;
    int data;
    int many;
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
        printf("[%d]:%d\n",p->data,p->many);
        p = p->next;
    }
}

void insert_many(struct number* p,struct number* w)
{
    struct number* q;
    p = p->next;
    while (p!=&head)
    {
        if (p->data==w->data)
        {
            p->many++;
            return;
        }
        p = p->next;
    }
    q = insert_pos(&head,w);
    insert(q,w);
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
        p->many=1;
        insert_many(&head,p);
    }
    printasc(&head);
    return 0;
}