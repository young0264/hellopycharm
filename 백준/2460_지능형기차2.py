arr=[]
res=0

for _ in range(10):
    a,b=map(int, input().split())
    res+=b
    res-=a
    arr.append(res)
print(max(arr))
