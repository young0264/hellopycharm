from collections import deque
r,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]#방문처리그래프
ans = [[0]*c for _ in range(r)]#거리넣을그래프
dxs,dys = [0,0,1,-1],[1,-1,0,0]
s1,s2 = 0,0
for i in range(r):
    for j in range(c):
        if graph[i][j]==2:
            s1,s2 = i,j
def in_range(x,y):
    return 0<=x<r and 0<=y<c and graph[x][y]==1 #and not visited[x][y]
def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i] , dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx,ny))
                ans[nx][ny] = ans[dx][dy]+1

bfs(s1,s2)##그래프0 visited0인거는 -1로
for i in range(r):
    for j in range(c):
        if  graph[i][j]==1 and not visited[i][j]:
            ans[i][j] = -1
for i in ans:
    print(*i)