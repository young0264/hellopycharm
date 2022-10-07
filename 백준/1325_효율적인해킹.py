from collections import deque
import sys
input = sys.stdin.readline
def bfs(x):
    visited =[]
    queue = deque()
    visited.append(x)
    queue.append(x)
    cnt = 0
    while queue:
        next = queue.popleft()
        cnt +=1
        for i in graph[next]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return len(visited)

n , m =map(int,input().split())
res=[0]*n

graph=[[] for i in range(n+1)]
for i in range(m):
    a , b = map(int,input().split())
    graph[b].append(a)
answer=[]
result=[]
for i in range(n):
    answer.append(bfs(i))
for i in range(n):
    if max(answer) == answer[i]:
        result.append(i)
print(*result)


    ##
#for i in range(1,n):
#    if graph[i] != [] :
#        res[i] = len(bfs(i)) #시작노드가 인덱스로 길이담기. 최대길이 인덱스출력
#print(bfs(1))
#answer=[]
#for i in range(1,n):
#    if res[i] == max(res):
#        answer.append(i)
#print(*answer)