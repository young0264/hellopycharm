def in_range(x,y):
    return 0<=x<n and 0<=y<n
import sys
input = sys.stdin.readline
dx = [0,1,0,-1] #행  #동남서북
dy = [1,0,-1,0] #열
num_dir = 1
n = int(input())
location = int(input())
graph = [[0]*n for _ in range(n)]
x , y = 0,0
graph[0][0] = n**2
answer =0,0
for i in range(n**2-1,0,-1):
    nx = x+dx[num_dir]
    ny = y+dy[num_dir]
    if in_range(nx,ny) and not graph[nx][ny] :#방문처리 된거 방문안하도록!
        graph[nx][ny] = i
        x,y=nx,ny
    else:   #범위를 벗어나면
        num_dir = (num_dir+3)%4
        nx = x + dx[num_dir]
        ny = y + dy[num_dir]
        graph[nx][ny] = i
        x, y = nx, ny
    if graph[nx][ny] == location:
        answer = nx+1,ny+1
if n**2 == location:
    answer = 1,1
for i in graph:
    print(*i)
print(*answer)
