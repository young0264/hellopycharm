from collections import deque
A , B = map(int,input().split())
dx = []
def in_range(x):
    return 1<=x<=10**9
cnt = 0
def bfs(x):
    global B,cnt
    q = deque()
    visited = []
    q.append(x)
    visited.append(x)
    while q:
        cnt += 1
        for _ in range(len(q)):
            next = q.popleft()
            if in_range(next):
                a = next*2
                b = next*10 + 1
                q.append(a)
                q.append(b)
                if a == B :
                    print(cnt+1)
                    exit(0)
                if b == B :
                    print(cnt+1)
                    exit(0)
    print(-1)
    exit(0)
bfs(A)

