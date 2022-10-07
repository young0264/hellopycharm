from collections import deque
import sys,time
start = time.time()
input = sys.stdin.readline
r , c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
q = deque()
dx = [1,0]
dy = [0,1]
x,y = 0,0
visited[0][0] = 0
def in_range(x,y):
    return 0<=x<r and 0<=y<c
def bfs(x,y):
    q.append((x,y))
    while q:
        for t in range(len(q)):
            a,b = q.popleft()
            for next in range(1,graph[a][b]+1):
                for i in range(2):
                    nx = a + dx[i]*next
                    ny = b + dy[i]*next
                    if in_range(nx,ny) and visited[nx][ny] == 0 :
                        q.append((nx,ny))
                        visited[nx][ny] = visited[a][b] + 1
                    if nx == r-1 and ny == c-1:
                        print(visited[r-1][c-1])
                        exit(0)
bfs(0,0)