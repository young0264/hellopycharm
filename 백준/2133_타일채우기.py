n = int(input())

dp = [0]*(n+1)
dp[2] = 3

for i in range(3,n+1):
    if not i%2 :    #나누어 떨어지는 짝수구간이면
        dp[i]+=dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i] += 2*dp[j]    ###-2 뒤가아니라 -4뒤의것과 비교를 해야하고 거기에 *2
        dp[i] += 2
print(dp[n])