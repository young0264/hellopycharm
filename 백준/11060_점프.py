from collections import deque
n = int(input())
arr = list(map(int,input().split()))
visited = [-1]*n    #visited에 저장된값을 쓴다는 점에서 dp와 bfs탐색 둘다 포함
def bfs(x):
    #dx = 0 #현재위치
    q = deque()
    visited[x]=0
    q.append(x)
    while q:
        next = q.popleft()  #현재좌표
        for i in range(1,arr[next]+1):
            nx = next + i
            if nx < n and visited[nx] == -1 :
                q.append(nx)
                visited[nx] = visited[next]+1
bfs(0)
print(visited[-1])

bfs(0)
