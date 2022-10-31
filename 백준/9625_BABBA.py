n = int(input())
dp = [[0,0] for _ in range(46)]
dp[0] = 1,0
dp[1] = 0,1
for i in range(2,46):
    a,b = dp[i-1]
    c,d = dp[i-2]
    dp[i] = a+c, b+d
# print(dp[n], sep=' ')
for i in dp[n]:
    print(i, end=' ')