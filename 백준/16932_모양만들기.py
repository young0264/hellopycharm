from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dxs, dys = [0,0,1,-1],[1,-1,0,0]
dic = dict()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(x,y,cnt):
    visited[x][y] = cnt
    que = deque()
    que.append((x,y))
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i],
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = cnt
                que.append((nx,ny))

#visited의 숫자에따라 영역 구별하기
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i,j,cnt)

#dic에 영역별(key)로 영역의 크기(value)를 저장
for i in range(n):
    for j in range(m):
        if visited[i][j] > 0:
            if not visited[i][j] in dic:
                dic[visited[i][j]] = 1
            else:
                dic[visited[i][j]] += 1

#그래프의 0인부분만 보고 상하좌우를 체크, 영역별 최대크기를 초기화해준다.
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0: #그래프 0위치에서 상하좌우
            brr= []
            for t in range(4):
                nx,ny = i+dxs[t], j+dys[t]
                if in_range(nx,ny) and visited[nx][ny]:
                    brr.append(visited[nx][ny])
            res = 0
            for k in (set(brr)):
                res += dic[k]
            answer = max(answer,res+1)

print(answer)