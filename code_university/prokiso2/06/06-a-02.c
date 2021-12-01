#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next;
    struct number* prev;
    int data;
    };

struct number head;

void print_tail()
{
    struct number* p;
    
    p = head.prev;
    while(p!=&head)
    {
        printf("%d,",p->data);
        p = p->prev;
    }
}

void add_list(struct number input)
{
    struct number* p;
    p = (struct number *)malloc(sizeof(struct number));
    if (p==NULL)
    {
        printf("out of memory\n");
        exit(1);
    }

    if (head.next==&head)
    {
        *p = input;
        head.next=p;
        head.prev = p;

        p->next = &head;
        p->prev = &head;

    }
    else
    {
        *p = input;
        p->next = &head;
        p->prev = head.prev;
        head.prev = p;
    }
    

}
int main()
{
    int i;
    struct number x;

    head.next = &head;
    head.prev = &head;
    
    printf("input 5 numbers:\n");

    for (i==0;i<5;i++){

        scanf("%d",&x.data);

        add_list(x);
    }
    printf("number list:");
    print_tail();
    return 0;
}