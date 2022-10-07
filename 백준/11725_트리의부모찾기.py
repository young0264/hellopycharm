from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
graph=[[]for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)      #그래프선언끝
    graph[b].sort()
    graph[a].sort()

res=[0]*(n+1)
visit=[0]*(n+1)
def bfs(x):
    visit[x] = True
    q = deque()
    q.append(x)
    while q:
        next = q.popleft()
        for i in graph[next]:
            if not visit[i]:
                #visited.append(next)
                q.append(i)#그냥i값?
                visit[i]=True
                res[i]=next


bfs(1)
print(*res[2::])