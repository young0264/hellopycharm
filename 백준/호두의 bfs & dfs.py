#bfs 3/1
from collections import deque

queue = deque()
queue.append((start,0))

while queue:
 node,depth = queue.popleft()
 visit[node] = True
 for next in graph[node]:
   if not visit[next]:
    q.append((next,depth+1))
    visit[next] = True
##############

queue = deque()
queue.append((start,0))
visit[start] = True
while queue:
 node,depth = queue.popleft()

 for next in graph[node]:
   if not visit[next]:
    q.append((next,depth+1))
    visit[next] = True


 ##############

 #dfs
def dfs(node):
    visit[node] = True
    for next in graph[node]:
        if not visit[next]:
            dfs(next)