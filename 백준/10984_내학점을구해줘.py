import sys
sys.setrecursionlimit(10000)
t = int(input())
for i in range(t):
    n=int(input())
    arr = []
    brr = []
    ar=[]
    h = 0
    for i in range(n):
        a,b=map(float,input().split())
        h += a
        arr.append(a*b)
        brr.append(b)
    print(int(h),'%.1f'%(sum(arr)/h))
