n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (i + 1) for i in range(len(triangle))]
dp[0][0] = triangle[0][0]
for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[len(triangle) - 1]))
