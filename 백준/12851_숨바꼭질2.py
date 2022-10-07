from collections import deque

subin, sister = map(int,input().split())

visited = [[-1,0] for _ in range(100001)]
def in_range(x):
    return 0<=x<=100000
def bfs(x):
    visited[x][0] += 1
    visited[x][1] = 1
    que = deque()
    que.append(x)
    while que:
        dx= que.popleft()
        arr = [dx+1,dx-1,2*dx]
        for nx in arr:
            if in_range(nx) and visited[nx][0] == -1:
                visited[nx][0] = visited[dx][0] + 1
                visited[nx][1] = visited[dx][1]
                que.append(nx)
            elif in_range(nx) and visited[nx][0] == visited[dx][0]+1 :
                visited[nx][1] +=  visited[dx][1]
bfs(subin)
print(visited[sister][0])
print(visited[sister][1])