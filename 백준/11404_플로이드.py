import sys
n = int(input())
m = int(input())
answer_graph = [[m]*n for _ in range(n)]
answer = [[sys.maxsize]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    answer_graph[a][b] = c
#끄악
for i in answer_graph:
    print(*i)

for i in range(n):
    for j in range(n):
        for k in range(n):#j,k
            answer_graph[j][k] = min(answer_graph[j][k],answer_graph[j][i]+answer_graph[i][k])
print()

for i in answer_graph:
    print(*i)