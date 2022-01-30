#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256

struct number
{
    struct number *next;
    struct number *prev;
    int data;
};

int d;

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
        if (p->data >= w->data)
        {
            return p;
        }
        p = p->next;
    }
    return &head;
}
void printasc(struct number *p,FILE *fp_out)
{
    p = p->next;
    while (p != &head)
    {
        fprintf(fp_out, "%d\n", p->data);
        p = p->next;
    }
}

int main()
{
    head.next = &head;
    head.prev = &head;

    struct number *p, *q;

    FILE *fp,*fp_out;
    char s1[MAX_LINE];
    int count=0;

    fp = fopen("11-b-02.txt", "r");
    fp_out = fopen("11-b-02_out.txt", "w");

    if (fp == NULL || fp_out == NULL)
    {
        printf("open error.");
        exit(1);
    }

    printf("CAN open.\n");
    while (fgets(s1,MAX_LINE,fp) != NULL)
    {
        p = (struct number *)malloc(sizeof(struct number));
        p->data = (int)(atof(s1));
        q = insert_pos(&head, p);
        insert(q, p);
        printf("%d\n",count++);
    }
    printf("CAN make.\n");

    fclose(fp);
    printasc(&head,fp_out);
    fclose(fp_out);

    return 0;
}
