import sys

while True:
    t = int(input())
    if t==0:
        exit(0)
    INF = -sys.maxsize
    dp = [INF]*t
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        if i==0:
            dp[0] = n
        else:
            dp[i] = max(n,dp[i-1]+n)
    answer = max(dp)
    print(answer)




    # dp = [[-sys.maxsize]*t for _ in range(t)]
    # arr = []
    # if t == 0:
    #     break
    # for i in range(t):
    #     n = int(input())
    #     dp[i][i] = n
    #     answer = max(answer,n)
    #     arr.append(n)
    # for i in range(t):
    #     for j in range(i+1,t):
    #         dp[i][j] = dp[i][j-1] + arr[j]
    #         answer = max(answer, dp[i][j])
    # print(answer)
