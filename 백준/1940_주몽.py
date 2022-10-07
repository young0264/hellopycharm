# 정렬후 두개의값을 왼쪽pos 오른쪽pos를 조여가며 값을 구하면 됨
n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))
right = n - 1
left = 0
cnt = 0
while left < right: #여기에 =이 있으면 안돼
    sum_value = arr[left] + arr[right]
    if sum_value > m:
        right -= 1
    elif sum_value == m:
        cnt += 1
        right -= 1
    else:
        left += 1
        sum_value -= arr[left]

print(cnt)
