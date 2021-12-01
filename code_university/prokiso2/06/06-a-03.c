#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next;
    struct number* prev;
    int data;
    };

int d,i;

struct number head;

void print_all(struct number* p)
{    
    p = p->next;
    while(p!=&head)
    {
        printf("[p:%p,bp:%p,fp:%p,data:%d]\n",p,p->prev,p->prev,p->data);
        p = p->next;
    }
}
void insert(struct number* p,struct number* w)
{
    w->next = p;
    w->prev = p->prev;

    p->prev->next = w;
    p->prev = w;
}

int main()
{
    head.next = &head;
    head.prev = &head;

    printf("input numbers:\n");

    struct number* p;

    for (;scanf("%d",&d)!=EOF;)
    {   
        p=(struct number *)malloc(sizeof(struct number));
        p->data=d;
        insert(&head,p);
    }
    print_all(&head);
    return 0;
}