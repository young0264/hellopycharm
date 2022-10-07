from collections import deque
from itertools import combinations
import sys

def input():
    return sys.stdin.readline().rstrip()

def in_range(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y]

def bfs():#해당방문지점을 min값으로 초기화
    global max_depth
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) and graph[nx][ny] != 1:
                visited[nx][ny] = visited[dx][dy]+1
                #max_depth = max(max_depth,visited[dx][dy])#최대방문값
                que.append((nx,ny))

n , m = map(int,input().split()) #연구소크기,바이러스개수
graph = [list(map(int,input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
sec_locate = []##2의위치

for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            sec_locate.append((i,j))

answer = sys.maxsize
for i in combinations(sec_locate,m):
    #한번의 조합경우의수. 위치들
    que = deque()
    visited = [[0] * n for _ in range(n)]
    max_depth = -1
    flag = True

    for dx,dy in i: #i하나가 m개만큼뽑은거
        que.append((dx,dy))
        visited[dx][dy] = 1

    bfs()

    for i in range(n):
        for j in range(n):
            max_depth = max(max_depth,visited[i][j])
            if graph[i][j] != 1 and not visited[i][j]:
                flag = False
    if flag:
        answer = min(answer,max_depth-1)#그중최소값

if answer == sys.maxsize:
    print(-1)
    exit(0)
print(answer)
#만약 그래프가1이 아닌데 방문을 안했다.
#5,6,7
