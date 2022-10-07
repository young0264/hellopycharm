from collections import deque
n , m =map(int,input().split())
kevin = [[]for _ in range(n+1)]
for i in range(m):  #n,m???###############
    a,b=map(int,input().split())
    kevin[a].append(b)
    kevin[b].append(a)
answer = []
def bfs(x):
    q = deque()
    visited=[x]
    num =[0]*(n+1)
    q.append(x)
    while q:
        next = q.popleft()
        for i in kevin[next]:
            if i not in visited:
                num[i] = num[next]+1
                visited.append(i)
                q.append(i)
    answer.append(sum(num))
for i in range(1,n+1):
    bfs(i)
for i in range(n):
    if min(answer)==answer[i]:
        print(i+1)
        exit(0)
