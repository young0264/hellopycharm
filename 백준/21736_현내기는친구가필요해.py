import sys
sys.setrecursionlimit(10**6)
def in_range(x,y):
    return  0<= x <r and 0<= y < c
def dfs(x,y):
    global cnt
    if in_range(x,y) and campus[x][y] != 'X' and visited[x][y]==0:#이래야 방문가능
        visited[x][y] = True
        if campus[x][y] == 'P' :
            cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)



r , c =map(int,input().split())
campus = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(r):
    for j in range(c):
        if campus[i][j] == 'I':
            dfs(i,j)
if cnt == 0:
    print('TT')
    exit(0)
print(cnt)