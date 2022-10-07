from collections import deque
n = int(input())
visited = [0 for _ in range(2000000)]
def circ(now,i):
    arr=[now+1, now-1, now//2, now//3 ]
    if i==2:
        if now%2:
            return False
    elif i==3:
        if now%3:
            return False
    return arr[i]

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        dx = que.popleft()
        for i in range(4):
            if circ(dx,i):
                nx = circ(dx,i)
                if nx == 1:
                    print(visited[dx])
                    exit(0)
                if not visited[nx] :
                    visited[nx] = visited[dx]+1
                    que.append(nx)
if n ==1:
    print(0)
    exit(0)
bfs(n)