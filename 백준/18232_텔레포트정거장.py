from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
def in_range(x):
    return 0< x <= n
def bfs(x):
    visited = [0 for i in range(n+1)]
    visited[x] += 1
    que = deque()
    que.append(x)
    while que:
        node = que.popleft()
        if node == e:
            print(visited[node]-1)
            exit(0)
        value = [node-1,node+1]
        if teleport[node]:
            value+=teleport[node]
        for i in range(len(value)):
            nx = value[i]
            if in_range(nx) and not visited[nx]:
                visited[nx] = visited[node]+1
                que.append(nx)

n,m = map(int,input().split())
s,e = map(int,input().split())
teleport = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    teleport[a].append(b)
    teleport[b].append(a)
bfs(s)