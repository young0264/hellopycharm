from collections import deque
q = deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
shark = 0,0
for i in range(n): #상어위치찾기
    for j in range(n):
        if graph[i][j] == 9 :
            shark = i,j
dx, dy = [1,-1,0,0],[0,0,1,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y): #각 방향에서 시작할거야
    q.append((x,y))
    stomach = 0
    while q:
        a,b = q.popleft()
        for i in range(4) :
            nx,ny = dx[i]+a , dy[i]+b
            if not in_range(nx,ny):
                continue
            if graph[nx][ny] > graph[a][b]:
                continue
            if  graph[a][b] > graph[nx][ny]:#상어가 크면, 이동+먹기
                stomach += 1
                a,b = nx,ny


