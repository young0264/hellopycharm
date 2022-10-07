n = int(input())
dp = [0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] += dp[j-1]*dp[i-j]
print(dp[-1])

#서로다른 bst개수는 왼쪽에 들어가는갯수*오른쪽에들어가는갯수