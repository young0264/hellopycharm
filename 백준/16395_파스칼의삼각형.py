r,c = map(int,input().split())

dp = [[0]*31 for _ in range(30)]
for i in range(30):
    dp[i][0] = 1
for i in range(1,30):
    for j in range(1,30):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
# for i in dp:
#     print(*i)

print(dp[r-1][c-1])
