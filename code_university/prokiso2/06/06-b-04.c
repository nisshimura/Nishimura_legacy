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
void remov(struct number* p,int index)
{
    int i;
    p = head.next;
    for (i==0;i!=index-1;i++)
    {
        if (p==&head)
        {
            printf("List doesnot have the index number:%d\n",index);
            return;
        }
        p = p->next;
    }
    
    p->next->next->prev = p;
    p->next = p->next->next;
}
void print_all(struct number* p)
{    
    p = p->next;
    while(p!=&head)
    {
        printf("[p:%p,bp:%p,fp:%p,data:%d]\n",p,p->prev,p->prev,p->data);
        p = p->next;
    }
}

int main()
{
    head.next = &head;
    head.prev = &head;

    printf("State Input:\n");

    struct number* p,* q;

    for (;scanf("%d",&d)!=EOF;)
    {   
        p=(struct number *)malloc(sizeof(struct number));
        p->data=d;
        insert(&head,p);
    }
    for (;scanf("%d",&d)!=EOF;)
    {   
        remov(&head,d);
    }  
    print_all(&head);
    return 0;
}