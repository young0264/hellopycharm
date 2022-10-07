#   서로간에 최단거리로 이동함에 있어
#   가장 긴 시간이 걸리는 육지 두곳에 묻혀있다
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x,y):
    cnt=0
    q = deque()
    visited[x][y] = True
    q.append([x,y])
    max_n = 0##
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= a or nx<0 or ny >= b or ny<0:
                continue
            if graph[nx][ny] == 'W':
                continue
            if visited[nx][ny]==1:
                continue
            visited[nx][ny]=True
            graph[nx][ny] = graph[x][y] + 1
            #max_n = graph[nx][ny] ##
            q.append([nx,ny])
    return graph[x][y]
a,b = map(int,input().split())
graph=[]
result = 0
for i in range(a):
    graph.append(list(input().strip()))
    
for i in range(a):
    for j in range(b):#쳌
        if graph[i][j] != 'W':
            visited = [[0] * b for _ in range(a)]##
            graph[i][j] = 0 ##
            visited[i][j] = 1
            result = max(result, bfs(i,j))
            print(result)
print(result)


