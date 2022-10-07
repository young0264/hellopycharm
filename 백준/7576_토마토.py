from collections import deque
def in_range(x,y):
    return 0<=x<r and 0<=y<c
c,r = map(int,input().split())
graph =[list(map(int,input().split())) for _ in range(r)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
visited = [[0]*c for _ in range(r)]
res = []
def bfs(x,y):
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if in_range(nx,ny) :
                if graph[nx][ny] == 0 :#and graph[nx][ny]==-1:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[a][b]+1   #이전꺼+1
                    res.append(graph[nx][ny])
#-1해서 출력
emergency = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            q.append((i,j))
        if graph[i][j]==0:
            emergency = 7

for i in range(r):
    for j in range(c):
        bfs(i,j)
for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            print(-1)
            exit(0)
if emergency == 0:
    print(0)
    exit(0)
else:
    print(max(res)-1)
#for i in graph:
#    print(i)
#print(max(res)-1)