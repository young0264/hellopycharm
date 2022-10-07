import sys
input = sys.stdin.readline
from collections import deque
q = deque()
n,m,h = map(int,input().split())#열,행,높이
graph = []
cnt = 0
for _ in range(h) :
    s = [list(map(int,input().split())) for _ in range(m)]
    graph.append(s)
dx,dy,dh = [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
def bfs():
    global cnt
    while q:
        cnt += 1
        for _ in range(len(q)):
            z,x,y = q.popleft() #높이,행.열 #현재위치
            for i in range(6):
                nz, nx, ny = dh[i]+z, dx[i]+x, dy[i]+y
                if in_range(nx,ny,nz):
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = 1
                        q.append((nz,nx,ny))

def check(x):   #x숫자가 있는지 찾기
    for t in range(h):
        for i in range(m):
            for j in range(n):
                if graph[t][i][j] == x:
                    return True
    return False

def in_range(x,y,height):#행,열,높이
    return 0<=x<m and 0<=y<n and 0<=height<h

for t in range(h):#높이
    for i in range(m):#행
        for j in range(n):#열
            if graph[t][i][j] == 1:#1,5,3
                q.append((t,i,j))   #시작위치를 넣어주고#높이,행,열


if not check(0):
    print(0)
    exit(0)
bfs()
if check(0):
    print(-1)
    exit(0)
print(cnt-1)