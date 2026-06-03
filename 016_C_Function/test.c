// gcc -o test test.c

#include <stdio.h>
#include <time.h>
#define INF 1e8

int main()
{
    clock_t start, end;

    int cnt = 0;
    double total;
    start = clock();

    for ( int i = 0; i < INF ; ++i )
        cnt += i;

    end = clock();
    total = ((double)end - start / CLOCKS_PER_SEC) / 1000000;
    printf("%f\n", total);

    return 0;

}