#include <stdio.h>
#include <stdlib.h>

int ashiba[10] = {0};
int cost[10] = {0};

int efficiency_asiba(int now, int limit)
{
    int i;
    int move1, move2;

    if (now>=limit)
    {
        return cost[now-1];
    }
    if (now==0)
    {
        ;
    }
    else if (now==1)
    {
        move1 = cost[now - 1] + abs(ashiba[now - 1] - ashiba[now]);
        cost[now] = move1;
    }
    else
    {
        move1 = cost[now - 1] + abs(ashiba[now - 1] - ashiba[now]);
        move2 = cost[now - 2] + abs(ashiba[now - 2] - ashiba[now]);


        if (move1>=move2)
        {
            cost[now]=move2;
        }
        else
        {
            cost[now]=move1;
        }
    }
    efficiency_asiba(now+1,limit);
}
int main()
{
    int i;
    int n;
    printf("input N:");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &ashiba[i]);
    }
    printf("Minimum cost is %d", efficiency_asiba(0,n));

    return 0;
}