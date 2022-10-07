import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n      #dp배열의 값은 해당위치에 있을때의 최댓값이다.
dp[0] = arr[0]  #초기값설정
for i in range(1,n):
    dp[i]=max(dp[i-1]+arr[i],arr[i])
print(dp)
print(max(dp))

#arr = [2, 1, -4, 3, 4,-4, 6, 5, -5, 1]
#dp  = [2, 3, -1, 3, 7, 3, 9, 14, 9, 10]

#[-2,-1,3,-3,4]
#[-2,-1,3,-3,4]
#