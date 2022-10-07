n= int(input())
def factorial(n):
    result = 1
    if n > 0 :
        result = n*factorial(n-1)
        # n==0일때 factorial(n) = 1
    return result
print(factorial(n))

###

def f(x):
    cnt = x-1
    while cnt :
        x *= cnt
        cnt-=1
    return x
print(f(5))