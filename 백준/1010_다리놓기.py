#def f(x):
#    k = 0
#    res = 1
#    while x >k:
#        res *= x-k
#        k += 1
#    return res
# dp를 활용한 두번째 방법
n = int(input())
dp = [[0]*31 for _ in range(31)]

for i in range(31):
    dp[1][i] = i
for i in range(2,31):
    for j in range(i,31):
        dp[i][j] = dp[i-1][j-1]+dp[i][j-1]

for _ in range(n):
    a,b = map(int,input().split())
    print(dp[a][b])