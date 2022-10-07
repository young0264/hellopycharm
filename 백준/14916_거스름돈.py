n = int(input())
mok = n//5
res = 10000000
if n == 1 or n==3 :
    print(-1)
    exit(0)
if n<5:
    print(n//2)
    exit(0)
else:
    for i in range(0, mok +1):
        cnt = 0
        x = n - (i*5)
        if x%2 == 0:
            cnt += x//2
            cnt += i
            #print(cnt)
            res = min(res, cnt)
        else:
            continue
    if res == 0:
        print(-1)
        exit(0)
    print(res)

