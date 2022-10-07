import sys
N,K = map(int,input().split())
arr = [0]*1000000
left,right = sys.maxsize,0
for _ in range(N):
    a,b = map(int,input().split())
    left,right = min(left,b-1), max(right,b-1)
    arr[b-1]=a
start = 0
ans = -sys.maxsize
sum_value = 0
max_value = -sys.maxsize
for i in range(right):
    sum_value += arr[i]
    if  i-start+1 == 2*K+1:
        max_value = max(max_value,sum_value)
        ans = max(ans,max_value)
        sum_value -= arr[start]
        start +=
print(ans)
