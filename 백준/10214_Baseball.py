n = int(input())
res=0
for i in range(n):
    for _ in range(9):
        a,b=map(int,input().split())
        res += a
        res -= b

    if res > 0 :
        print('Yonsei')
    elif res < 0:
        print('Korea')
    else:
        print('Draw')