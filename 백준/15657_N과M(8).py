n , m = map(int,input().split())
arr=sorted(list(map(int,input().split())))

def dfs(start,box):
    if len(box) == m:
        print(*box)
        return
    for i in range(start,len(arr)):
        dfs(i,box+[arr[i]])

dfs(0,[])