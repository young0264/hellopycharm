import sys
from collections import deque
input = sys.stdin.readline
n , m , start = map(int,input().split())
arr=[[]*(n+1) for i in range(n+1)]
for i in range(m):
    a , b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
q = deque()
visited = [0]*(n+1)
res = [0]*(n+1)
q.append(start)
cnt = 1
while q:
    node = q.popleft()
    res[node] = cnt
    cnt += 1
    visited[node] = True
    for next in sorted(arr[node]):
        if not visited[next]:
            visited[next]=1
            q.append(next)

           # print(q)
for i in res[1:]:
    print(i)