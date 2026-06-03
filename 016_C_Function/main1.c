#include <stdio.h>
#include <windows.h>

int main()
{
    int a = 10;
    int b = 40;

    // 명시적 연결을 위한 변수
    HINSTANCE hInstDll;
    int(*sum)(int, int);
    int(*diff)(int, int);

    hInstDll = LoadLibrary("libmath.so");

    sum = (int(*)(int, int))GetProcAddress(hInstDll,"sum");
    diff = (int(*)(int, int))GetProcAddress(hInstDll,"diff");

    printf("sum : %d\n", (*sum)(a,b));
    printf("diff : %d\n", (*diff)(a,b));

    return 0;
}