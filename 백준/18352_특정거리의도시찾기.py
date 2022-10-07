from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split()) #도시의개수N,도로의개수 M,거리정보 K,출발번호
arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
depth_arr = [0]*(n+1)
def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = 1
    while que:
        node = que.popleft()
        for next in arr[node]:
            if not visited[next]:
                visited[next] = visited[node]+1
                que.append(next)

for i in range(m):
    s1,s2 = map(int,input().split())
    arr[s1].append(s2)

bfs(x)
flag = 0
for i in range(n+1):
    if visited[i] == k+1:
        print(i)
        flag+=1
if not flag:
    print(-1)


