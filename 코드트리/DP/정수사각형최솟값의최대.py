n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]##dp정의 : 현재위치까지의 최솟값의 최댓값
dp[0][0] = graph[0][0]  ##초기값
for j in range(1,n):
    dp[0][j] = min(dp[0][j-1],graph[0][j])
for i in range(1,n):
    dp[i][0] = min(dp[i-1][0],graph[i][0])


for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(max(dp[i-1][j],dp[i][j-1]),graph[i][j])
print(dp[n-1][n-1])
