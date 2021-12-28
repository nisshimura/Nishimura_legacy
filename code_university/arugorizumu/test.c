#include <stdio.h>
#include <stdlib.h>
#define MAXLINE 256

struct tree
{
    struct tree *left;
    struct tree *right;
    int data;
    int depth;
};

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

void print_tree(struct tree *top,int depth)
{
    int i;

    if(top==NULL)
    {
        return ;
    }
    /* 右の子孫ノードを表示 */
    print_tree(top->right, depth+1);

    /* 深さをスペースで表現 */ 
    for(i = 0; i < depth; i++)
    {
        printf("  ");
    }

    /* ノードのデータを表示 */
    printf("%d\n", top->data);

    /* 左の子孫ノードを表示 */
    print_tree(top->left, depth+1);

    depth++;
}

int main()
{
    int n,i;
    struct tree* y=NULL;
    struct tree* top=NULL;

    printf("Input n : ");
    scanf("%d",&n);

    int arr[n];

    for (int i = 0; i < n; i++) arr[i] = i+1;
    do {
        top=NULL;
        for (int i = 0; i < n; i++) 
        {
            printf(" %d",arr[i]);
            y=(struct tree *)malloc(sizeof(struct tree));
            y->data = arr[i];
            y->left = NULL;
            y->right = NULL;

            top = add_tree(top,y);
        }
        print_tree(top,0);
    } while (get_zyunretsu(arr, n));
    return 0;
}