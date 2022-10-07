#경우의수. 하나도 배치하지 않는 경우도 하나의 경우의 수로 친다.
#import sys
#sys.setrecursionlimit(10**6)

n = int(input())
#0,1,2로 나누어주고
dp = [[0]*3 for _ in range(n)]
dp[0][1], dp[0][0],dp[0][2] = 1,1,1
#탑다운
#def D(n,k):
#    if n==1:
#        return 1
#    elif dp[n][k]!=0:
#        return (dp[n][k])%9901
#    if k==1:
#        dp[n][k] = (D(n-1,2) + D(n-1,0))%9901
#    elif k==2:
#        dp[n][k] = (D(n-1,1) + D(n-1,0))%9901
#    elif k==0 :#k==0
#        dp[n][k] = (D(n-1,2) + D(n-1,1) + D(n-1,0))%9901
#    return dp[n][k] ##
#ans = 0
#for i in range(3):
#    ans += D(n,i) #[n]행의 k : 0,1,2에 대한 합들
#print(ans%9901)

for i in range(1,n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901
print(dp)
print(sum(dp[n-1])%9901)
