import sys
from collections import deque
input = sys.stdin.readline

n , m , start = map(int,input().rstrip().split())
arr = [[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
res = [0 for _ in range(n)]

for i in range(m):
    a , b = map(int,input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)
#for i in range(n+1):
#    arr[i].sort(reverse=True)
cnt = 1
stack = deque({start})

while stack:
    next = stack.pop()
    visited[next] = True
    if not res[next-1]:
        res[next-1] = cnt
        cnt+=1

    for i in reversed(sorted(arr[next])):
        if not visited[i]:
            stack.append(i)
#def dfs(x):
#    global cnt
#    visited[x] = 1
#    res[x-1] = cnt
#    cnt+=1
#    for i in sorted(arr[x]):
#        if not visited[i]:
#            dfs(i)
#
#dfs(start)
for i in res:
    print(i)


