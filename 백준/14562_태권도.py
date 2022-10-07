from collections import deque
def move(a,b,i):
    dx = [a*2,a+1]
    dy = [b+3,b]
    return (dx[i],dy[i])
res = []
def bfs(n1,n2):
    dp = [[0] * 200 for _ in range(200)]
    que = deque()
    que.append((n1,n2))
    dp[n1][n2] = 1
    while que:
        dx,dy = que.popleft()
        for i in range(2):# 0~1
            nx,ny = move(dx,dy,i)
            if 0<=nx<200 and 0<=ny<200 and not dp[nx][ny] :
                if nx == ny:
                    res.append(dp[dx][dy])
                    return
                dp[nx][ny] = dp[dx][dy]+1
                que.append((nx,ny))

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    bfs(a,b)
for i in res:
    print(i)
