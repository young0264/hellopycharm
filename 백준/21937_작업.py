import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

n , m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

work_pos = int(input())
visited = [-1]*(n+1)
answer = 0
def dfs(x):
    for nx in graph[x]:
        if 0< nx <= n  and visited[nx] == -1:
            visited[nx] = visited[x] +1
            visited[x] = 0
            dfs(nx)
visited[work_pos] = 0
dfs(work_pos)
for i in visited:
    if i>0 :
        answer += i
print(answer)
