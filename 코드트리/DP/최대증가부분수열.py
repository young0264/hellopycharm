#n = 5
#dp = [-1]*n
#a = [2,3,0,1,4]
#
#dp[0]=0
#
#for i in range(1,n):
#    for j in range(i):
#        if dp[j] != -1 and i-j >= a[j]: #점프를 해야될거리가 점프할수있는거리보다 작거나 같아야
#            dp[i] = max(dp[i],dp[j]+1)
#print(max(dp))

n = int(input())
a = list(map(int,input().split()))
