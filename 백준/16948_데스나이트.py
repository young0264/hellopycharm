from collections import deque
def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y] = 0
    while q :
        x,y= q.popleft()
        #q.append(graph[x][y])
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1 :

                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
                #print(graph[nx][ny])
           #     if (nx,ny) == (c,d):
           #         return cnt
           # if graph[nx][ny] =
           # else:return -1
n=int(input())
graph = [[-1]*n for _ in range(n)]
a,b,c,d = map(int,input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
bfs(a,b)
print(graph[c][d])

