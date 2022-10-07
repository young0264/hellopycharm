import sys
from collections import deque
sys.setrecursionlimit(10**6)
def in_range(x,y):
    return 0<=x<n and 0<=y<n and  graph[x][y]==1 and visited[x][y]==False
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
len_graph = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):   #대륙에 숫자붙히기
    global now
    visited[x][y] = True
    graph[x][y] = now
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if in_range(nx,ny):
            dfs(nx,ny)
        #else:return        여기서 리턴하면 왜 숫자가 증가하는거지## 오늘!꼭!
        #else: continue
answer = 0
def bfs(x,y):   #대륙의 각 칸에서 bfs실행. 다른칸이 나올때까지/글로벌변수 하나놓고 최솟값저장
    global answer
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        cnt = 0
        for i in range(4):
            nx,ny = a+dx[i], b+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                cnt += 1
                q.append((nx,ny))
        print(cnt)
bfs(0,0)





graph[0][0] = 1
visited[0][0] = True
now = 1
for i in range(10):
    for j in range(10):
        if visited[i][j]==0 and graph[i][j] == 1:
            dfs(i,j)#재귀적으로 깊이 파고드는거야
            now += 1
for i in graph:
    print(*i)


#확장하기 실패
#for i in range(n):
#   for j in range(n):
#       if graph[i][j]==True:
#           for k in range(4):
#               nx = i+dx[k]
#               ny = j+dy[k]
#               if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
#                   graph[nx][ny] = graph[i][j]
#for i in graph:
#    print(*i)

