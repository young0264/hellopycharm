n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, len(arr) - 1
cnt = 0

while left < right:
    sum_value = arr[left] + arr[right]
    if sum_value == x:
        cnt += 1
        right -= 1
    elif sum_value < x:
        left += 1
    else : #sum_value > x
        right -= 1
print(cnt)