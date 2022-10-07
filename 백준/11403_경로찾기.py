# 플로이드워셜
# 3충for문을 사용. 2차원배열.
from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1 or(graph[i][k]==1 and graph[k][j]==1):
                #min(graph[i][j] , graph[i][k] + graph[k][j])
                graph[i][j] = 1

for i in graph:
    print(*i)