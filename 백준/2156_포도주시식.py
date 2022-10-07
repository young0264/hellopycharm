n = int(input())
dp = [0]*(n)
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)
if n==1 :
    print(arr[0])
elif n==2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(dp[1],arr[2]+dp[0],arr[1]+arr[2])
    dp[2] = max(arr[2]+arr[0],arr[1]+arr[2],arr[0]+arr[1])

    for i in range(3,n):
        dp[i] = max(dp[i-3]+arr[i]+arr[i-1], dp[i-1], dp[i-2]+arr[i])
    print(max(dp))
