import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n , m , start = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    a , b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
stack = deque([start])
res = [-1]*n

def dfs(x,depth):
   # global cnt
    visited[x] = 1
    res[x-1] = depth
   # cnt+=1
    for i in reversed(sorted(arr[x])):
        if not visited[i]:
            dfs(i,depth+1)

dfs(start,0)
#print(res)
for i in res:
    print(i)


