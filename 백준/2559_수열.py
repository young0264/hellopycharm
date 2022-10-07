import sys
N,K = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
sum_value = 0
max_value = -sys.maxsize
for i in range(len(arr)):
    sum_value += arr[i]
    if  i-start+1 == K:
        max_value = max(max_value,sum_value)
        sum_value -= arr[start]
        start += 1
print(max_value)
