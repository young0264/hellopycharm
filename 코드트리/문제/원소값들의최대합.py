n, m = map(int,input().split())
arr = [0] + list(map(int,input().split()))
answer = 0

for i in range(1,n+1):
    num = m
    now = i
    res = 0
    while num:
        num -= 1
        res += arr[now]
        now = arr[now]
    answer = max(answer, res)

print(answer)


