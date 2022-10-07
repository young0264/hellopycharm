n = int(input())
res=[]
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    res.append(arr.pop(7))
for i in res:
    print(i)