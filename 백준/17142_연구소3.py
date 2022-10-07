from itertools import combinations
from collections import deque
import sys
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and visited[x][y]==-1 and graph[x][y]!=1

def bfs(vlist): #m개의 바이러스 리스트 입력
    global ans
    visited = [[-1]*n for _ in range(n)]
    que = deque()
    max_value = 0
    for i in vlist:
        a,b=i
        que.append(i)
        visited[a][b] += 1
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny=dxs[i]+dx,dys[i]+dy
            if can_go(nx,ny):#2도이동
                visited[nx][ny] = True
                que.append((nx,ny))###
                visited[nx][ny] = visited[dx][dy] + 1
                if graph[nx][ny] == 0:
                    max_value = max(max_value,visited[nx][ny])
    s = list(sum(visited,[]))
    if s.count(-1) == list(sum(graph,[])).count(1):
        ans = min(ans,max_value)

n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
virus = []
MS = sys.maxsize
dxs,dys = [1,-1,0,0],[0,0,1,-1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))

ans = MS
for v in combinations(virus,m): #m가지의 바이러스를 뽑은 경우의수
    bfs(v)
if ans == MS:
    print(-1)
else:
    print(ans)
