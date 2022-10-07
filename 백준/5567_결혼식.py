from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def bfs(x):
    que=deque()
    que.append(x)
    visited[x] = 1
    while que:
        dx = que.popleft()
        if graph[dx]:
            for a in graph[dx]:
                if 0<=a<n and not visited[a]:
                    visited[a] = visited[dx]+1
                    que.append(a)

        #for i in range(4):
            #nx,ny =dx+dxs[i] , dy+dys[i],
            #if in_range(nx,ny) and not visited[nx][ny]:
            #    visited[nx][ny] = visited[dx][dy] + 1
            #    que.append((nx,ny))

n = int(input())
m = int(input())
graph =[[] for _ in range(n)]
visited =[0]*n
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

bfs(0)
cnt = 0

for i in visited:
    if i == 2 or i==3:
        cnt += 1
print(cnt)