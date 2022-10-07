from collections import deque
r, c, t = map(int,input().split())
graph = [list(input()) for _ in range(r)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0<=x<r and 0<=y<c
def zero():# 폭탄설치
   for i in range(r):
        for j in range(c):
            graph[i][j] = 'O'
def finding():#폭탄위치넣기
    for i in range(r):
        for j in range(c):
            if graph[i][j] =='O':
                que.append((i,j))
def bomb(): #폭탄터트리기
    while que:
        dx,dy = que.popleft()
        graph[dx][dy] = '.'
        for i in range(4):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) :
                if graph[nx][ny]=='O':
                    graph[nx][ny] = '.'
que = deque()
res = []
def go(x):
    if x==1:
        finding()
    elif x%2 == 0:
        zero()
    elif x%2 == 1:
        bomb()
        finding()
for i in range(1,t//5+t%5+1):
    go(i)
for i in graph:
    print(*i,sep='')

