n = int(input())

if n==1:
    print(1)
    exit(0)
dp = [0]*(n+1)
dp[1],dp[2] = 1,2
for i in range(3,n+1):
    dp[i] = dp[i-1]%15746 + dp[i-2]%15746

print(dp[n]%15746)
