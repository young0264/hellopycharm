#시간초과뜨네

from collections import deque
import sys

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs():
    global n1,n2
    cnt = 0
    que = deque()
    que.append((n1,n2))
    visited[n1][n2] = 1
    while que:
        cnt += 1
        for _ in range(len(que)):
            a,b = que.popleft()
            for i in range(8):
                nx , ny = a+dx[i] , b+dy[i]
                if in_range(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = visited[a][b]+1
                    que.append((nx,ny))
    return
input = sys.stdin.readline
n , m = map(int,input().split())
n1,n2 = map(int,input().split())
n1,n2 = n1-1,n2-1
dx,dy = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,-2,-1,1,2]
bt = []
visited = [[0] * n for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    bt.append((a,b))
ans = []
bfs()
for x,y in bt:
    ans.append(visited[x][y]-1)
print(*ans)