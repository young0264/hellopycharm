import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(input()) for _ in range(n)]
#visited=[[False]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
ex = graph
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,l):
    if 0<=x<n and 0<=y<n :
        if graph[x][y] == l :
            if graph[x][y] == 'R':
                visited[x][y] = 'G'
            else:
                if graph[x][y] == 'G' or 'B':
                    visited[x][y] = graph[x][y]
            graph[x][y] = False
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                dfs(nx,ny,l)
            return True #이거
    return False
def dfs2(x,y,l):
    if 0<=x<n and 0<=y<n :
        if visited[x][y] == l :
            visited[x][y] = False
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                dfs2(nx,ny,l)
            return True #이거
    return False
#for i in range(n):
#    for j in range(n):
#        if graph[i][j] =='R':
#            visited[i][j] = 'G'
#        else : visited[i][j] = graph[i][j]
#
ans=0
unn=0
print(graph)
for i in range(n):
    for j in range(n):
        if dfs(i,j,'R') == True:
            ans+=1
        if dfs(i,j,'G') == True:
            ans+=1
        if dfs(i,j,'B') == True:
            ans+=1
print(visited)
for i in range(n):
    for j in range(n):
        if dfs2(i,j,'G') == True:
            unn +=1
        if dfs2(i,j,'B') == True:
            unn +=1
print(ans,unn)




#        if dfs1(i,j,'R') == True:
#            ans+=1
#        if dfs1(i,j,'G') == True:
#            ans+=1
#        if dfs1(i,j,'B') == True:
#            ans+=1
#        if dfs(i, j, 'R' or 'G') == True:
#            unn += 1
#        if dfs(i, j, 'B') == True:
#            unn += 1
#print(ans,unn)
#