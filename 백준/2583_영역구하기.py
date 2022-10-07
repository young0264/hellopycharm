import sys
sys.setrecursionlimit(10**6)

m , n, k = map(int,input().split())
#arr =[ list(map(int,input().split())) for i in range(k)]
graph =[[1]*n for _ in range(m)]
for t in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(m):
        for j in range(n):
            if a<= j <c and b<= i <d:
                graph[i][j] = 0
            #elif a<= j <2 and 1<= i <5:
            #    graph[i][j] = 0
            #elif 4<= j <6 and 0<= i <2:
            #    graph[i][j] = 0
#print(graph)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt
    graph[y][x]=False
    #방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if  0<= nx < n  and 0 <= ny < m and graph[ny][nx]==1:
            cnt += 1
            #graph[ny][nx] = False#방문처리
            dfs(nx,ny)
cnt = 1
res = []
total = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(j,i)
            res.append(cnt)
            cnt = 1
            total +=1
res.sort()
print(total)
print(*res)