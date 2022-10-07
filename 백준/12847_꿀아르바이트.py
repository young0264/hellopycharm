import sys
start = 0
N,K = map(int,input().split())
arr = list(map(int,input().split()))

sum_value = 0
max_value = -sys.maxsize
answer = -sys.maxsize
for i in range(len(arr)):
    sum_value += arr[i]
    if i-start+1 == K:
        max_value = max(max_value,sum_value)
        sum_value -= arr[start]
        start += 1
        answer = max(answer,max_value)
print(answer)
