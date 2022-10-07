n, m = map(int, input().split())
arr = []
if n:
    arr = list(map(int, input().split()))

answer = 0

sum_value = 0
for i in arr:
    if sum_value + i < m:
        sum_value += i
    elif sum_value + i ==m:
        sum_value = 0
        answer += 1
    else:
        answer += 1
        sum_value = i
if sum_value:
    answer += 1
print(answer)
