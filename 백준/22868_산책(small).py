from collections import deque
n , m = map(int,input().split())
arr = [[] for _ in range(n+1)]
answer = 0
for _ in range(m+1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def in_range(x):
    return 0<x<=n


def bfs(x):
    global answer
    que = deque()
    que.append((x,[0]*(n+1)))
    que[0][1] = 



