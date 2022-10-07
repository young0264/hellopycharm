import sys
sys.setrecursionlimit(10**6)
#input = sys.stdin.readline


r,c = map(int,input().split())
#r,c=r-1,c-1

graph = [list(map(int,input())) for _ in range(r)]
#print(graph)
dx,dy = [1,-1,0,0],[0,0,1,-1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c

def dfs(x,y):
    if x == r-1:
        print('YES')
        exit(0)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if in_range(nx,ny) and not graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            #print(nx,ny)
            dfs(nx,ny)

for j in range(c):
    if not graph[0][j]:
        visited = [[0] * c for _ in range(r)]
        dfs(0,j)
print('NO')
exit(0)