#include <stdio.h>
#include <stdlib.h>

struct data
{
    struct data* fp;
    struct data* bp;
    int num;
    };


void insert(struct data* p,struct data* w)
{
    w->fp = p;
    w->bp = p->fp;

    p->fp->bp = w;
    p->bp = w;
}

void push(struct data* sentinel,int n)
{
    struct data* q;
    q = (struct data *)malloc(sizeof(struct data));
    if (q==NULL)
    {
        printf("out of memory\n");
        exit(1);
    }
    printf("push %d\n",n);
    q->num = n;

    q->fp = sentinel;
    q->bp = sentinel->bp;

    sentinel->bp->fp=q;
    sentinel->bp=q;
}

int pop_queue(struct data* sentinel)
{
    printf("pop %d\n",sentinel->fp->num);
    sentinel->fp->fp->bp = sentinel;
    sentinel->fp = sentinel->fp->fp;
}
int pop_stack(struct data* sentinel)
{
    printf("pop %d\n",sentinel->bp->num);
    sentinel->bp->bp->fp = sentinel;
    sentinel->bp = sentinel->bp->bp;
}
void print_data(struct data* sentinel)
{
    struct data* p;
    p = (struct data *)malloc(sizeof(struct data));
    printf("stored nums:");

    p = sentinel->bp;
    while(p!=sentinel)
    {
        printf("%d ",p->num);
        p = p->bp;
    }
    printf("\n");
}

int main()
{
    int i;
    struct data sentinel;
    sentinel.fp = sentinel.bp = &sentinel;
    push(&sentinel,1);
    print_data(&sentinel);
    push(&sentinel, 2);
    print_data(&sentinel);
    push(&sentinel, 3);
    print_data(&sentinel);
    pop_queue(&sentinel);
    print_data(&sentinel);
    pop_stack(&sentinel);
    print_data(&sentinel);
    return 0;
}