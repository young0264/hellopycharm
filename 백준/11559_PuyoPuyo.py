# 같은 알파벳값에대해 bfs진행. -> 4개이상이면 .으로초기화 ->
#밑에서 위로 tmp 해서 채워넣기
from collections import deque
graph = [list(input()) for _ in range(12)]#12줄
s_graph = [[0]*6 for _ in range(12)]
for i in range(12):
    for j in range(6):
        s_graph[i][j] = graph[i][j]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
def in_range(x,y):
    return 0<=x<12 and 0<=y<12
visited = [[0]*6 for _ in range(12)]
def bfs(x,y):
    que = deque()
    cnt=0
    que.append((x,y))
    visited[x][y] = True
    while que:
        dx,dy = que.popleft()
        for _ in range(4):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny]:# and graph[nx][ny]=:
                que.append((nx,ny))
                visited[nx][ny] = True
                bomb_cnt(dx,dy,nx,ny)
                if cnt >=4:
                    bomb(x,y)


def bomb_cnt(x,y,nx,ny): #같으면 cnt증가
    # 반복문후 cnt가 4이상이면 visited가 1인곳을 . 으로바꾸고
    global cnt
    if s_graph[x][y] == s_graph[nx][ny] :
        cnt += 1
        
def bomb(dx,dy):
    for i in range(12):
        for j in range(6):
            if visited[i][j]:
                s_graph[i][j] = '.'
                visited[i][j]=False

def move(x,y):
    for j in range(6):
        for i in range(11,-1,-1):
            if not s_graph[i][j] == '.' :
                s_graph[x][y] = s_graph[i][j]
                s_graph[i][j] = '.'

