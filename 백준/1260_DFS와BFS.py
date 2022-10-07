from collections import deque
import sys
sys.setrecursionlimit(100000)
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  ##노드와.인접노드가 적혀있는 그래프생성끝
    graph[b].sort()
    graph[a].sort()
visit=[0]*(n+1)

def dfs(x):
    visit[x] = True
    print(x,end=' ')

    for i in graph[x]:
        if not visit[i]:
            dfs(i)

def bfs(x):
    q=deque()
    visited=[]
    q.append(x)
    while q:
        node=q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    for i in visited:
        print(i,end=' ')
dfs(v)
print()
bfs(v)