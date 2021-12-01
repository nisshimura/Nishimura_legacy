#include <stdio.h>
#include <stdlib.h>

struct number
{
    struct number* next_id,* next_ave;
    struct number* prev_id,* prev_ave;
    int id;
    int math;
    int sci;
    int eng;
    float ave;
    };

int a,b,c,d;

struct number head;

void insert_id(struct number* p,struct number* w)
{
    w->next_id = p;
    w->prev_id = p->prev_id;

    p->prev_id->next_id = w;
    p->prev_id = w;
}

void insert_ave(struct number* p,struct number* w)
{
    w->next_ave = p;
    w->prev_ave = p->prev_ave;

    p->prev_ave->next_ave = w;
    p->prev_ave = w;
}
struct number*insert_pos_id(struct number* p,struct number* w)
{   
    p = p->next_id;
    while (p!=&head)
    {
        if (p->id>=w->id)
        {
            return p;
        }
        p = p->next_id;
    }
    return &head;
}
struct number*insert_pos_ave(struct number* p,struct number* w)
{   
    p = p->next_ave;
    while (p!=&head)
    {
        if (p->ave>=w->ave)
        {
            return p;
        }
        p = p->next_ave;
    }
    return &head;
}
void print_sorted_id(struct number* p)
{    
    printf("[ID]\n");
    p = p->next_id;
    while(p!=&head)
    {
        printf("ID:%d,Math:%d,Science:%d,English:%d\n",p->id,p->math,p->sci,p->eng);
        p = p->next_id;
    }
}

void print_sorted_ave(struct number* p)
{    
    printf("[Average]\n");
    p = p->next_ave;
    while(p!=&head)
    {
        printf("Average:%f,ID:%d\n",p->ave,p->id);
        p = p->next_ave;
    }
}

int main()
{
    head.next_id = &head;
    head.prev_id = &head;

    head.next_ave = &head;
    head.prev_ave = &head;

    struct number* p,* q,* r;


    while(1)
    { 
        printf("InputID,Math,Science,English:");
        scanf("%d %d %d %d",&a,&b,&c,&d);
        if (a<0)
        {
            break;
        }
        p=(struct number *)malloc(sizeof(struct number));
        p->id=a;
        p->math=b;
        p->sci=c;
        p->eng=d;
        p->ave=(float)(b+c+d)/3.0;
        q = insert_pos_id(&head,p);
        r = insert_pos_ave(&head,q);
        insert_id(q,p);
        insert_ave(r,p);
    }
    print_sorted_id(&head);
    print_sorted_ave(&head);
    return 0;
}