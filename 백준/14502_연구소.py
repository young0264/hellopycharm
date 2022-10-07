#백트래킹으로 3개를 뽑은후 탐색하기
#0이면 3개를 뽑고 3개의 위치를 1로 바꾸고 bfs진행.-> 그 3개를 다시 0으로 초기화
# ->global 변수에 max값 갱신
from collections import deque
import copy
def in_range(x,y):
    return 0<=x<r and 0<=y<c
r , c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(box): #x,y는
    if box==3:  # 0을 1로 바꿀때마다 cnt += 1
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 2:
                    q.append((i,j)) #2일때의 위치를 넣고
        copy_graph = copy.deepcopy(graph)#그래프 초기화후 bfs실행(밖에나와있어도 q에 위치삽입되어있음)   q
        bfs(copy_graph)
        return

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0 :
                graph[i][j] = 1
                dfs(box+1)
                graph[i][j] = 0 #그래프는 원래모양대로
max_answer = 0
def bfs(graph):
    global max_answer
    now = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if in_range(nx,ny) and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = 2
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                now +=1
    max_answer = max(max_answer , now)

dfs(0)
print(max_answer)
