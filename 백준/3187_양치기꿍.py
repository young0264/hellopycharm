from collections import deque
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c and graph[x][y]!='#'

total_v = 0
total_k = 0
def bfs(x,y):
    global total_v, total_k
    v,k=0,0
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = dx[i]+a
            ny = dy[i]+b
            if in_range(nx, ny) and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny]=True
                if graph[nx][ny]=='v':
                    v+=1
                elif graph[nx][ny]=='k':
                    k+=1
    if v>=k:
        total_v += v
    else:
        total_k += k
for i in range(r):
    for j in range(c):
        bfs(i,j)
print(total_k,total_v)


