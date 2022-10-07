#6
#1 3 5 7 2 3
from bisect import bisect_left
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
ans = []
new_arr = []

for i in range(len(arr)):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        new_arr.append((len(dp)-1,arr[i]))#len,num
    else:
        k = bisect_left(dp, arr[i])
        dp[k] = arr[i]
        new_arr.append((k,arr[i]))#idx,num

print(len(dp))

max_value = len(dp)-1
for i in range(len(new_arr)-1, -1, -1):#dp길이가 cnt max값임
    if new_arr[i][0] == max_value:
        ans.append(new_arr[i][1])
        max_value -= 1

print(*reversed(ans))
