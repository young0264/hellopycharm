import sys
sys.setrecursionlimit(10**6)

n , m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
res=[]

def dfs(box):
    if len(box)==m:
        print(*box)
        #res.append(box)
        return
    for i in range(len(arr)):
        dfs(box+[arr[i]])
dfs([])

#for i in sorted(list(set(map(tuple,res)))):
#    print(*i)
