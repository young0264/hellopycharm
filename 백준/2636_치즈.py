#bfs(0,0)시작 -> 0탐색
#2중for문으로 1과 인접한게 방문처리된거면0으로 바꿔주고
#또 0에대해 탐색

from collections import deque
r,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
spare_graph = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        spare_graph[i][j] = graph[i][j]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
cnt = 0#cnt갯수하고 마지막queㅇㄴ에 들어잇는갯수출력
ans = []
def in_range(x,y):
    return 0<=x<r and 0<=y<c

def bfs():
    global cnt
    que = deque()
    que.append((0,0))
    visited[0][0] = True
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dxs[i]+dx, dys[i]+dy
            if in_range(nx,ny) and not visited[nx][ny] and not spare_graph[nx][ny]:
                visited[nx][ny] = True
                que.append((nx,ny))
def check():
    cnt=0
    for i in range(r):
        for j in range(c):
            if spare_graph[i][j]:
                for t in range(4):
                    nx,ny = i+dxs[t],j+dys[t]
                    if in_range(nx,ny) and visited[nx][ny] and spare_graph[i][j]:#인접한게방문한거면
                        spare_graph[i][j]=0
                        cnt+=1
    return cnt
res = []
ans = 0
while True:
    visited = [[0]*c for _ in range(r)]
    bfs()
    res.append(check())
    if res[-1]==0:
        break
    ans+=1
print(ans)
print(res[-2])





