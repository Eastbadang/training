// p.c
#include <math.h>

#define true (1)
#define false (0)

// typedef int bool

// bool isprime(int n)
int isprime(int n)
{
  int k;
  int l;
  if (n < 2) return false;
  if (n == 2 || n == 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  if (n < 9) return false;
  k = 5;
  l = (int)(sqrt((double)n) + 0.5);
  while (k <= l) {
    if (n % k == 0 || n % (k + 2) == 0) return false;
    k += 6;
  }
  return true;
}