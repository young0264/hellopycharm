# 대각선은 붙어있는게 아님 , 3<=n,m<=300
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def bfs(x,y):
    global flag
    que = deque()
    que.append((x,y))
    visited[x][y]=1
    z = 0

    #시작점
    for i in range(4):
        fx,fy = x+dxs[i],y+dys[i]
        if in_range(fx,fy) and new_graph[fx][fy] == 0:
            z+=1
    #graph 주위에 0이 있는 갯수만큼 빼서 newgraph로 초기화해주기

    #원래그래프를 기준으로 값을 비교하고 . new graph는 변경내용 임시 저장용.
    while que:
        dx,dy = que.popleft()
        zero_cnt = 0
        for i in range(4):
            nx,ny = dx+dxs[i] , dy+dys[i]
            if in_range(nx,ny) and graph[nx][ny]==0:
                zero_cnt += 1
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]:
                que.append((nx,ny))
                visited[nx][ny] = 1

                # for i in range(4):
                #     nnx,nny = nx+dxs[i], ny+dys[i]
                #     if in_range(nnx,nny) and graph[nnx][nny] == 0:
                #         zero_cnt += 1
                #         print("nnx,nny,zero_cnt",nx,ny,zero_cnt)
        new_graph[dx][dy] = graph[dx][dy] - zero_cnt

    #graph에 new그래프의 값을 복사

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0],

answer = 0

flag = 0
while True:
    visited = [[0] * c for _ in range(r)]
    new_graph = [[0] * c for _ in range(r)]
    cnt = 0     #bfs 갯수
    # print("graph")
    # for i in graph:
    #     print(*i)
    for i in range(r):
        for j in range(c):
            if graph[i][j] and not visited[i][j]:
                # print("i,j",i,j)
                flag = 1    #방문표시
                bfs(i,j)
                cnt += 1
    # print("cnt",cnt)
    answer += 1

    if cnt >= 2:
        print(answer-1)
        exit(0)
    elif cnt == 0 :
        break
    else :
        for i in range(r):
            for j in range(c):
                if new_graph[i][j] < 0:
                    graph[i][j] = 0
                else:
                    graph[i][j] = new_graph[i][j]

print(0)
