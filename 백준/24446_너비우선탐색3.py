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
res = [-1]*(n+1)
other =[0]*(n+1)
other_num = 1
q.append(start)
cnt = -1
while q:
    cnt+=1
    for i in range(len(q)):
        node = q.popleft()
        other[node]=other_num
        other_num+=1
        res[node] = cnt
        visited[node] = True
        for next in reversed(sorted(arr[node])):
            if not visited[next]:
                visited[next]=1
                q.append(next)

           # print(q)
answer = 0
for i in range(1,n+1):
    answer+=(res[i]*other[i])
print(answer)