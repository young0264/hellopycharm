def dfs1(x,y):#위아래보기
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '|':
        graph[x][y] = True
        dfs1(x+1,y)
        dfs1(x-1,y)
        return True
    return False

def dfs2(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '-':
        graph[x][y] = True
        dfs2(x,y+1)
        dfs2(x,y-1)
        return True
    return False

n , m = map(int,input().split())
graph = [ list(input()) for _ in range(n) ]
cnt = 0

for i in range(n):
    for j in range(m):
        if dfs1(i,j) == True:
            cnt += 1
        if dfs2(i,j) == True:
            cnt += 1
print(cnt)