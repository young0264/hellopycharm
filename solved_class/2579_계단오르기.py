t=int(input())
arr=[0]*301
dp=[0]*301
for i in range(t):
    arr[i] =(int(input()))

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[1]+arr[2],arr[0]+arr[2])
for n in range(3,t): #arr은 t-1배열까지있어.
    dp[n] = max(dp[n-3] + arr[n-1]+arr[n] , dp[n-2]+arr[n])
print(dp[t-1])

#왜 리스트에 제한을 두는지와
#왜 arr=[] arr.append(int(input)) 을 하면 안되는지->런타임에러