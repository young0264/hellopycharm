def f(n):
    if n==0 :
        return 0
    elif n==1 :
        return 1
    #else 도 안쓰고
#n이 2이상인경우
    return f(n-1) + f(n-2) #f(n) = 이 아니라 return을 하니되네


n=int(input())
print(f(n))