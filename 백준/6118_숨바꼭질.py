# 헛간번호, 헛간까지의거리, 같은거리에 있는 헛간 출력.
#거리는 visited 에 저장하는식으로 하고. 같은갯수출력, 헛갈번호는그중에 또 min값
from collections import deque
n , m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a , b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = 1  #이래해서 1빼는게
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        next = q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                visited[i] = visited[next] + 1
                q.append(i)

bfs(1)
goal = max(visited)
answer =[]
for i in visited:
    if i == goal:
        answer.append(visited.index(goal))
        answer.append(goal-1)
        x=visited.count(goal)
        answer.append(x)
        print(*answer)
        exit(0)
