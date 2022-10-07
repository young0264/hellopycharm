n = int(input())

a = 300
b = 60
c = 10
arr=[]
if n%c==0:
    arr.append(n//a)
    n=n%a
    arr.append(n//b)
    n=n%b
    arr.append(n//c)
    print(*arr)
else:
    print(-1)