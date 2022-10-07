# 0:이동, 1:벽, 2:사람, 3:비를피할수있는공간
from collections import deque
n, h, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n
def can_go(x,y):
    return in_range(x,y) and graph[x][y] != 1 and not visited[x][y]
def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if can_go(nx,ny):
                if graph[nx][ny] == 3 : #피를 피할 수 있는경우 2차원배열answer에 해당위치에 누적값 초기화
                    answer[x][y] = visited[dx][dy]
                    return True
                visited[nx][ny] = visited[dx][dy] + 1 # 3이아닌 can_go위치에 누적값초기화&방문처리
                que.append((nx,ny))
    answer[x][y] = -1   #3으로 리턴되지 않고 while문이 끝났으면 시작지점은 빠져나올 수 없는영역

dxs,dys = [1,-1,0,0],[0,0,1,-1]
answer = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            visited = [[0]*n for _ in range(n)]
            bfs(i,j)

for i in answer:
    print(*i)
