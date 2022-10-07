import sys
sys.setrecursionlimit(10**6)
def in_range(x,y):
    return 0<=x<r and 0<=y<c
def dfs(x,y):
    if in_range(x,y) and graph[x][y]=='#' and visited[x][y]==0:  # 이면은
        visited[x][y] = True    #무작정할게 아니라, 범위안에 먼저 든 후에 방문처리
        for i in range(4):  #탐색하기
            nx = dx[i]+x
            ny = dy[i]+y
            dfs(nx,ny)
        return True
    return False

dx = [0,0,1,-1]
dy = [1,-1,0,0]
t = int(input())
for _ in range(t):
    answer = 0
    r , c = map(int,input().split())
    graph =[list(input()) for _ in range(r)]
    visited = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            #if graph[i][j] == '#':
            if dfs(i,j):
                answer+=1
            #answer += 1
    print(answer)