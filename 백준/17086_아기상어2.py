from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while que:
        dx,dy,k = que.popleft()
        for i in range(8):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny] :
                visited[nx][ny] = visited[dx][dy]+1
                que.append((nx,ny,k+1))

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

r , c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dxs,dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,1,0]
que = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j]:
            que.append((i,j,0))
            visited[i][j] = 1
bfs()
print(max(map(max,visited))-1)


