// Ref. : https://kitae0522.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-C-%ED%95%A8%EC%88%98-%ED%98%B8%EC%B6%9C%ED%95%B4%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

int fibo(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibo(n-1) + fibo(n-2);
}