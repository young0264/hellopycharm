t = int(input())
dp = [1,5]

for i in range(t):
    n = int(input())
    if n>=3:
        print((5**(n-2))+2)
    else:
        print(dp[n-1])


