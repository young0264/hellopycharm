n , m = map(int,input().split())
def fac(x):
    i=1
    for k in range(1,x+1):
        i *= k
    return i

result = fac(n)//(fac(n-m)*fac(m))
print(result)