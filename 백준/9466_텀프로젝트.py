import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
answer = []
def dfs(idx):
    global res
    nx = arr[idx]-1
    visited[idx] = True
    resArr.append(idx)

    if visited[nx] :
        if nx in resArr:

            res += resArr[resArr.index(nx):]
        return
    else:
        dfs(nx)


for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    visited = [0]*n
    res=[]

    for j in range(n):
        if not visited[j] :
            resArr = []
            dfs(j)
    print((n-len(res)))


