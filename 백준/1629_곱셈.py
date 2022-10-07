a,b,c=map(int,input().split())
#res=a**b%c

def mul(a,b,c): #1승까지 내려버리는구만
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (mul(a, b//2, c)**2)%c
    else:
        return ((mul(a, b//2, c)**2)*a)%c

print(mul(a,b,c))