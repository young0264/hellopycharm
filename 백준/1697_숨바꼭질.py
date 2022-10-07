from collections import deque

n , k = map(int,input().split())
dist = [0]*(100001)
cnt=1
def bfs(x):
    q = deque()
    q.append(x)
    while q :
        next = q.popleft()
        if next == k :
            print(dist[next])
            break
        for nx in(next+1, next-1, next*2):
            if 0 <= nx <= 100000 and not dist[nx]:
                q.append(nx)
                dist[nx]=dist[next]+1
bfs(n)



