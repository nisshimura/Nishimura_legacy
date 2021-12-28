#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAXLINE 256

struct tree
{
    struct tree *left;
    struct tree *right;
    int data;
};

struct zyun
{
    struct zyun* next;
    int s[MAXLINE];
};

struct zyun* head;
struct zyun* tail;

void print_head(int n,int index)
{
    struct zyun* p;
    
    p = head;
    for (int i=0;i<index;i++)
    {
        p = p->next;
    }
    int i;
    printf("[");
    for (i = 0; i < n; i++) 
    {
        printf(" %d", p->s[i]);
    }
    printf("]\n");
}
void print_all(int n)
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

struct tree* add_tree(struct tree* top,struct tree* input)
{
    struct tree* p;
    int i;

    if (top==NULL)
    {
        top = input;
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
                break;
            }

            p = p->left;
        }

        else if (input->data > p->data)
        {
            if (p->right == NULL)
            {
                p->right = input;
                break;
            }
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

int print_tree(struct tree *top,int depth)
{
    int i,max=0;
    if (max<depth)
    {
        max = depth;
    }
    if(top==NULL)
    {
        return max;
    }
    print_tree(top->right, depth+1);
 
    for(i = 0; i < depth; i++)
    {
        printf("  ");
    }

    printf("%d\n", top->data);

    print_tree(top->left, depth+1);

    depth++;
}

int main()
{
    int n,i,j,depth,height[MAXLINE]={0},count=0,total;
    float zyo,ave;
    struct tree* y=NULL;
    struct tree* top=NULL;
    
    struct zyun* x;

    printf("Input n : ");
    scanf("%d",&n);

    int arr[n];

    for (int i = 0; i < n; i++) arr[i] = i+1;
    do {
        x=(struct zyun *)malloc(sizeof(struct zyun));
        top=NULL;
        for (int i = 0; i < n; i++) 
        {
            y=(struct tree *)malloc(sizeof(struct tree));
            printf(" %d",arr[i]);
            x->s[i] = arr[i];
        }
        add_zyun(*x);
        printf("\n");
    } while (get_zyunretsu(arr, n));

    printf("\n");

    do {
        struct zyun* p;
        p = head;
        while(p!=NULL)
        {
            top=NULL;
            int i;
            printf("[");
            for (i = 0; i < n; i++) 
            {
            printf(" %d", p->s[i]);
            y=(struct tree *)malloc(sizeof(struct tree));
            y->data = p->s[i];
            y->left = NULL;
            y->right = NULL;
            top = add_tree(top,y);
            }
            printf("]\n");
            depth = print_tree(top,0);
            printf("depth : %d\n",depth);
            height[count] = depth;
            p = p->next;
            count++;
        }
    } while (get_zyunretsu(arr, n));

    for (i=0;i<count;i++)
    {
        total += height[i];
    }
    printf("total : %d",total);
    ave = (float)total/count;
    printf("\nAverage : %f",ave);
    for (i=0;i<count;i++)
    {
        total += pow(height[i]-ave,2.0);
    }
    zyo = total/count;
    printf("\nDistribute : %f",zyo);

    return 0;
}