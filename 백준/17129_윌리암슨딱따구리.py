from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def bfs(x,y):
    que = deque()
    visited = [[0]*m for _ in range(n)]
    que.append((x,y))
    visited[x][y] = 1

    while que:
        dxs,dys = que.popleft()
        for i in range(4):
            nx,ny = dxs+dx[i],dys+dy[i]

            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]!=1 :
                if graph[nx][ny] > 1:
                    return visited[dxs][dys]

                visited[nx][ny]= visited[dxs][dys]+1
                que.append((nx,ny))
    return False

n,m = map(int,input().split())  #행,열
graph = [list(map(int,input())) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
s1,s2 = -1,-1
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            s1,s2=i,j
            break

ans = bfs(s1,s2)
if ans:
    print("TAK")
    print(ans)
else:
    print("NIE")




