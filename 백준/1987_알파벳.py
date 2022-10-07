r , c = map(int,input().split())
graph = []
for i in range(r):
    l = input()
    x = []
    for j in l:
        x.append(ord(j)-65)
    graph.append(x)
check = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [-1] * 26
visited[graph[0][0]] = True
def in_range(x,y) :
    return 0<=x<r and 0<=y<c  #행,열
def dfs(x,y,cnt):   #여기에 두면 재귀의 깊이에 따라 cnt를 셀 수가있어.
                    #재귀의 깊이가 깊어지는 max값을 초기화해서 출력하면돼
    global res
    res = max(cnt, res)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if in_range(nx, ny) and visited[graph[nx][ny]] == -1:
            visited[graph[nx][ny]] = True
           # print(visited)
            dfs(nx, ny, cnt+1)
            visited[graph[nx][ny]] = -1
            res=max(res, cnt)
res = 1
dfs(0,0,res)
print(res)
