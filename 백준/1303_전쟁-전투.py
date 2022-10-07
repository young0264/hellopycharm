#1흰W:팀, 2파랑B:적//W영역갯수 제곱+= / B영역갯수 제곱+=
from collections import deque
c,r = map(int,input().split())
in_graph = [list(input()) for _ in range(r)]
graph = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
def in_range(x,y):
    return 0<= x <r and 0<= y<c

for i in range(r):
    for j in range(c):
        if in_graph[i][j]=='W':
            graph[i][j] = 1
        elif in_graph[i][j]=='B':
            graph[i][j] = 2

def bfs(x,y):
    global cnt
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    cnt+=1
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dxs[i]+dx,dys[i]+dy
            if in_range(nx,ny) and not visited[nx][ny] and graph[dx][dy] == graph[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                que.append((nx,ny))
w_value = 0
b_value = 0

for i in range(r):
    for j in range(c):
        cnt = 0
        if not visited[i][j]:
            bfs(i,j)
            if graph[i][j] == 1  :
                w_value += cnt**2
            elif graph[i][j] == 2 :
                b_value += cnt**2

print(w_value,b_value)


