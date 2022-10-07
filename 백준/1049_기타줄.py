import sys
N, M = map(int, input().split())
min_price = sys.maxsize
mina, minb = 1001, 1001
x = 1001
for _ in range(M):
    a, b = map(int, input().split())
    mina = min(mina, a)
    minb = min(minb, b)
if minb*6 < mina :
    print(minb*N)
else:
    x = min(((N//6)+1)*mina,(N//6)*mina+(N%6)*minb)
    min_price = min(min_price,x)
    print(min_price)