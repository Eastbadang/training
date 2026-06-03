def sum(n):
    """computes a sum of integers from 1 to n"""
    if n == 1 : return 1
    else : return n+sum(n-1)

def prod(n):
    """computes a product of integers from 1 to n"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print("Hello World!")
print("1+2+...+10=",sum(10))
print("1*2*...*10=",prod(10))