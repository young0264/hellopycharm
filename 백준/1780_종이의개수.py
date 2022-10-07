n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
m1 = 0
zero = 0
p1=0
def dfs(x,y,n):
    global m1,zero,p1
    now = graph[x][y]
    rest = n//3
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j]!=now:
                dfs(x,y,rest)
                dfs(x,y+rest,rest)
                dfs(x,y+rest*2,rest)
                dfs(x+rest,y,rest)
                dfs(x+rest,y+rest,rest)
                dfs(x+rest,y+rest*2,rest)
                dfs(x+rest*2,y,rest)
                dfs(x+rest*2,y+rest,rest)
                dfs(x+rest*2,y+rest*2,rest)
                return

    if now == -1:
        m1+=1
    if now == 0:
        zero+=1
    if now == 1:
        p1+=1
dfs(0,0,n)
print(m1,zero,p1, sep='\n')
