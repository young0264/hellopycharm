import sys
sys.setrecursionlimit(1000000)
n,m=map(int,sys.stdin.readline().split())
graph={i: [] for i in range(1,n+1)}
visited = [0]*(n+1)  # visited = [False] * (N + 1)
cnt=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):#,visited):
    visited[start]= True

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)


   #     if visited[i]==False:
   #         dfs(i,visited)
  #  if visited[i] not in graph[start]:
   #     dfs(i,)




#def dfs():
#    start=[i for i in range(1,n+1)] #노드 머리들 들어있음
#    need_visit=[]#adj = [[] for _ in range(N + 1)]
#    need_visit.append(start)
#    while need_visit:
#        node=need_visit.pop()
#        if node not in visited:
#            visited.append(node)
#            for i in graph[node]:
#                need_visit.append(i)
#    return visited