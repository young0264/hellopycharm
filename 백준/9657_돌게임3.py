import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(1001) #n을사용하면 인덱스에러.

dp[1],dp[3],dp[4] = True, True, True

for i in range(5,n+1):
    if dp[i-1] and dp[i-3] and dp[i-4] == True:
        dp[i] = False
    else:
        dp[i] = True
if dp[n]:
    print('SK')
else:
    print('CY')
