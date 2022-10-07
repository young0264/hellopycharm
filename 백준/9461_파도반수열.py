#규칙 찾기. 규칙만 찾으면 쉬움

import sys
input

t = int(input())
arr = [1,1,1,2,2,3]
l = [int(input()) for _ in range(t)]
n = max(l)
for i in range(6,n):
    x = arr[i-1] + arr[i-5]
    arr.append(x)
#print(arr)
for j in l :
    print(arr[j-1])