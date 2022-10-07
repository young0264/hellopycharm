n = int(input())
for i in range(n):
    r, e, c = map(int,input().split())
    res = e-c
    if r > res :
        print("do not advertise")
    elif r == res:
        print("does not matter")
    else :
        print("advertise")