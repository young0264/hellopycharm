#q는 True인거에서 시작
from collections import deque
n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
limit, a, b = map(int,input().split())
a,b = a-1,b-1
virus = []
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def in_range(x,y):
    return 0<= x <n and 0<= y <n
for i in range(n):
    for j in range(n):
        if graph[i][j] :
            virus.append((i,j))
virus.sort()
q = deque(virus)
#print(graph)
cnt = 0
def bfs():
    global cnt
    while q:
        if cnt == limit:
            break
        for t in range(len(q)):
            a,b=q.popleft()
            for i in range(4):
                nx = a+dx[i]
                ny = b+dy[i]
                if in_range(nx,ny) and graph[nx][ny]==0 :
                    graph[nx][ny] = graph[a][b]
                    q.append((nx,ny))
        cnt +=1
#print(graph)

bfs()
print(graph[a][b])