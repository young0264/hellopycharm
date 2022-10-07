from collections import deque
r,c=map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dxs,dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,1,-1,-1]
def in_range(x,y):
    return 0 <= x < r and 0 <= y < c

def bfs(x,y):
    visited[x][y]=True
    que = deque()
    que.append((x,y))
    while que :
        dx,dy = que.popleft()
        for i in range(8):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) and  graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx,ny))
    return True
ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] and not visited[i][j]:
            if bfs(i,j):
                ans+=1

print(ans)





