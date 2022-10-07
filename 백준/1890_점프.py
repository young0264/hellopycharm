n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dx,dy = [0,1],[1,0]
k = graph[0][0]
dp[k][0],dp[0][k] = 1,1
#dp[0][0]= 1##초기값설정

for i in range(n):
    for j in range(n):
        for t in range(2):
            f = graph[i][j]
            nx,ny = dx[t]*f + i , dy[t]*f + j
            if i==n-1 and j==n-1:
                continue
            elif 0 <= nx < n and 0 <= ny < n:
                dp[nx][ny] += dp[i][j]

print(dp[n-1][n-1])