from collections import deque
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]  #0번째는 비어있음
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
visited = [False]*(n+1)
#print(visited)
def bfs(x):
    cnt=0
    q = deque()
    visited[x] = True
    q.append(x)
    while q:
        next = q.popleft()
        for i in graph[next]:   #인접한 인자들
            if not visited[i]:    #if i not in visited:    #방문을 안한 인자들이면
                q.append(i)    #q에 넣어주고
                visited[i] = True
                cnt+=1
    return cnt
print(bfs(1))