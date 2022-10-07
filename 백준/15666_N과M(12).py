n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = []
def dfs(start,box):
    if len(box) == m :
        res.append(box)
        return
    for i in range(start,len(arr)):
        dfs(i,box+[arr[i]])

dfs(0,[])
res=sorted(list(set(map(tuple,res))))
for i in res:
    print(*i)