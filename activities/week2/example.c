#include <stdio.h>


int count_until_N(int N)
{
    int x = 0;
    for (int i=0; i < N; i++)
        x += i;
    return x;
}

int main()
{
    int N = 100000000;
    count_until_N(N);
    count_until_N(N);

    printf("%d %d", count_until_N(N), N*(N-1)/2);
    return 0;
}

