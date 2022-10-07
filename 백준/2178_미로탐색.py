# 0,0에서 j-1,i-1까지
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
#graph = [list(map(int,input().split())) for _ in range(n)]
#graph = []
#for i in range(n):
#    graph.append(list(map(int,input())))
graph = [list(map(int,input())) for _ in range(n)]
#split()하면 연결되서 입력된다. 조심

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append((x,y))     #q에 (x,y)형태로 저장
    while q:
        x, y = q.popleft()
        for i in range(4):  #[nx][ny]
            nx = x + dx[i]      #(x,y)에서 상하좌우 탐색
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  #여기네
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1   #방문처리겸. 누적합
                q.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))






#def dfs(x,y,s):
#    if x<0 or x>=m or y<0 or y>=n :
#        return False
#    if arr[x][y]==0:
#        return False
#    s+=arr[x][y] #s에 11111이렇게 입력
#    #arr[x][y] = 0
#    dfs(x+1,y,s)
#    dfs(x-1,y,s)
#    dfs(x,y+1,s)
#    dfs(x,y-1,s)
#    #result.append(''.join(s))
#    result.append(s) #하나가완성되면 result배열에 한덩어리 입력
#    #return True
#for i in range(n):
#    for j in range(m):
#        dfs(j,i,"")
#
#print(len(result))