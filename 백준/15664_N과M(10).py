n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = []
def dfs(start,box):
    if len(box) == m:
        res.append(box)
        return
    for i in range(start,len(arr)):
        dfs(i+1, box + [arr[i]])
dfs(0,[])
#print(set(res))
ans = list(map(tuple,res))
for i in sorted(list(set(ans))):
    print(*i)
