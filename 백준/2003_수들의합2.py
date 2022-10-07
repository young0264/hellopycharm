n,m =  map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
left,right=-1,0
sum_value = 0

for left in range(n):
    while right<n and sum_value < m:
        sum_value += arr[right]
        right += 1
    if sum_value ==m:
        cnt += 1
        sum_value -= arr[left]
    else:
        sum_value -= arr[left]

print(cnt)