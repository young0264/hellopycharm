from bisect import bisect_left
n = int(input())
arr = [-1]*500
dp = [-1]

for _ in range(n):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    arr[a] = b
for i in range(len(arr)):# dp 처음 값 초기화
    if  arr[i]!=-1:
        dp[0] = arr[i]
        break
for i in range(len(arr)):
    if arr[i]!=-1:
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            k = bisect_left(dp,arr[i])
            dp[k] = arr[i]
print(n-len(dp))