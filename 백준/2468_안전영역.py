import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y,high):
    visited[x][y] = True
    for i in range(4):
        nx , ny = dx[i]+x , dy[i]+y
        if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] > high:
            dfs(nx,ny,high)
    return

maxhigh = 0
for i in range(n):
    for j in range(n):
        maxhigh = max(maxhigh,graph[i][j])
max_cnt = 0
for h in range(maxhigh):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h :
                cnt +=1
                dfs(i,j,h)
    max_cnt = max(max_cnt,cnt)
print(max_cnt)