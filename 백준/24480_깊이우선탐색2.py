import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n , m , start = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a , b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
#print(arr)
visited=[0]*(n+1)
flag = 1
res = [0]*n
def dfs(x):
    global flag
    visited[x] = 1
    res[x-1] = flag
    flag +=1
    for i in reversed(sorted(arr[x])):
        if not visited[i]:
            dfs(i)
dfs(start)
for i in range(n):
    print(res[i])

