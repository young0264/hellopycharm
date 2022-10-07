from collections import deque

def bfs(a,b):
    queue = deque()
    b1_cnt = 1
    visited[a][b] = True
    queue.append((a,b))
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            if 0 <= nx <n  and  0 <= ny < m :
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True #방문체크
                    queue.append((nx,ny))
                    b1_cnt += 1
    return b1_cnt
#6,5 5칸6줄
n , m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
graph =[list(map(int,input().split())) for _ in range(n)]
dx =[1,-1,0,0]
dy =[0,0,1,-1]
cnt,res_cnt = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            res_cnt = max(res_cnt,bfs(i,j))
print(cnt)
print(res_cnt)




