t = int(input())
def dfs(x,cnt):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = 1
            cnt = dfs(nx,cnt+1)
    return cnt
for i in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited[1]=1
    ans = dfs(1,0)
    print(ans)

