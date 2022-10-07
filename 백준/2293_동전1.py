# 동전을 적당히 사용해 그 가치의 합이 k원이 되도록. 몇개라도 사용가능
# 순서만 다른거는 같은 경우의수.
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
#dp = [[0]*k for _ in range(n)]
res = [0]*k
arr =[]

for _ in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(k):
        t = j+1-arr[i]

        if t == 0:
            #dp[i][j] = 1
            res[j] += 1
        elif t > 0:
            #dp[i][j] = res[t-1]
            res[j] += res[t-1]
print(res[-1])


