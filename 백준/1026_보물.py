n = int(input())
a = sorted(list(map(int,input().split())))
b = list(map(int,input().split()))
b.sort(reverse=True)
res=[]
for i in range(n):
    res.append(a[i]*b[i])

print(sum(res))
