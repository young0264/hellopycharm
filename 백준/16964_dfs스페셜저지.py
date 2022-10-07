import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(ans):
    tmp = ans.popleft()
    if not ans:
        print(1)
        exit(0)
    visited[tmp] = 1
    for i in range(len(graph[tmp])):
        if ans[0] in graph[tmp] and visited[ans[0]]==0:
            dfs(ans)
    return False

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = deque(map(int,input().split()))
if ans[0] != 1:
    print(0)
    exit(0)
if not dfs(ans):
    print(0)
