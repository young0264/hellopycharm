n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx,dy = [0,1],[1,0]#행열
def in_range(x,y):
    return 0<=x<n and 0<=y<n #and not visited[x][y]

def dfs(x,y):
    if x == n - 1 and y == n - 1:
        return True
    for i in range(2):
        nx,ny = x+dx[i]*graph[x][y], y+dy[i]*graph[x][y]
        if in_range(nx,ny) and not visited[nx][ny]:
            #print(nx,ny)
            visited[nx][ny] = 1
            #if nx==n-1 and ny==n-1:
            #    #print("HaruHaru")
            #    #exit(0)
            #    return dfs(nx,ny)
            if dfs(nx,ny):
                return True
            else: False

visited[0][0]=1
#dfs(0,0)
#print("Hing")
if  dfs(0,0):
    print("HaruHaru")
else:
    print("Hing")