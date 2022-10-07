import sys
sys.setrecursionlimit(10**6)

n , m , k = map(int,input().split())
graph = [[0]*m for _ in range(n)]
#print(graph)
for i in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 1
def dfs(x,y):
    global cnt
    graph[y][x] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx < m and 0<= ny < n and graph[ny][nx]==1:
            dfs(nx,ny)
            cnt += 1
res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(j,i)
            res.append(cnt)
            cnt = 1
print(max(res))