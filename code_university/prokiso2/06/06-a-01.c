#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next;
    int data;
    };

struct number* head;
struct number* tail;

void print_head()
{
    struct number* p;
    
    p = head;
    while(p!=NULL)
    {
        printf("%d,",p->data);
        p = p->next;
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
    if (tail==NULL)
    {
        head = p;
    }
    else{
        tail->next=p;
    }
    tail = p;
    *tail = input;
    tail->next = NULL;
}
int main()
{
    int i;
    struct number x;
    printf("input 5 numbers:\n");
    for (i==0;i<5;i++){

        scanf("%d",&x.data);

        add_list(x);
    }
    printf("number list:");
    print_head();
    return 0;
}