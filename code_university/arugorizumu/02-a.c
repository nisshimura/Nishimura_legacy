#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define MAXLINE 256

struct zyun
{
    struct zyun* next;
    int s[MAXLINE];
    int depth;
};

struct tree
{
    struct tree* left;
    struct tree* right;
    int data;
    int depth;
    int s[][MAXLINE];
};
struct zyun* head;
struct zyun* tail;
void add_zyun(struct zyun input)
{
    struct zyun* p;
    p = (struct zyun *)malloc(sizeof(struct zyun));
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

struct tree* add_tree(struct tree* top,struct tree* input)
{
    struct tree* p;
    int depth=0,i;
    p = (struct tree *)malloc(sizeof(struct tree));
    if (p==NULL)
    {
        printf("out of memory\n");
        exit(1);
    }
    if (top==NULL)
    {
        top = input;
        top->depth = depth;
        return top;
    }
    
    p = top;
    while (1)
    {
        if (input->data < p->data)
        {
            if (p->left == NULL)
            {
                p->left = input;
                p->depth = depth;
                for (i=0;p->s[depth][i]==0;i++)
                {
                    p->s[depth][i] = p->data;
                }
                break;
            }
            depth++;
            p = p->left;
        }

        else if (input->data > p->data)
        {
            if (p->right == NULL)
            {
                p->right = input;
                p->depth = depth;
                for (i=0;p->s[depth][i]==0;i++)
                {
                    p->s[depth][i] = p->data;
                }
                break;
            }
            depth++;
            p = p->right;
        }
        else
        {
            printf("This number is exist.");
            break;
        }
    }
    return top;
}

void print_head(int n)
{
    struct zyun* p;
    
    p = head;
    while(p!=NULL)
    {
        int i;
        for (i = 0; i < n; i++) 
        {
        printf(" %d", p->s[i]);
        }
        printf("\n");
        p = p->next;
    }
}

void print_tree(struct tree *top,int count)
{
    int i,depth=0,data[MAXLINE]={0};
    struct tree* p;
    p = (struct tree *)malloc(sizeof(struct tree));
    if (p==NULL)
    {
        printf("out of memory\n");
        exit(1);
    }

    if(top == NULL)
    {
    return ;
    }
    
    print_tree(top->right,++depth);


    
}

int get_zyunretsu(int *arr, int n) {
    int left = n - 2;
    while (left >= 0 && arr[left] >= arr[left+1]) 
    {
        left--;
    }

    if (left < 0) 
    {
        return 0;
    }

    int right = n - 1;
    
    while (arr[left] >= arr[right]) 
    {
        right--;
    }

    int t = arr[left];
    arr[left] = arr[right];
    arr[right] = t;

    left++;
    right = n - 1;
    
    while (left < right) 
    {
    int t = arr[left];
    arr[left] = arr[right];
    arr[right] = t;

    left++;
    right--;
    }
    
    return 1;
}

int main()
{
    int n,i;
    struct zyun* x;
    struct tree* y;
    
    struct tree* top;
    struct tree* p;

    printf("Input n : ");
    scanf("%d",&n);

    int arr[n],k;

    for (int i = 0; i < n; i++) arr[i] = (i+1);
    do {
        x=(struct zyun *)malloc(sizeof(struct zyun));
        p = top;
        for (int i = 0; i < n; i++) 
        {
            y=(struct tree *)malloc(sizeof(struct tree));
            x->s[i] = arr[i];
            y->data = arr[i];
            y->left = NULL;
            y->right = NULL;
            p = add_tree(p,y);
            print_tree(p);
        }
        add_zyun(*x);
    } while (get_zyunretsu(arr, n));

    print_head(n);

    return 0;
}