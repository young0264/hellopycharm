n = int(input())
arr = list(map(int, input().split()))
sum_arr = [arr[0]] * n
sum_reverse_arr = [arr[n-1]] * n
max_value = 0
sum_value = sum(arr)
answer = 0
answer += sum_value - arr[0]
for i in range(1, n):
    sum_arr[i] = sum_arr[i - 1] + arr[i]

for i in range(n-2,-1,-1):
    sum_reverse_arr[i] = sum_reverse_arr[i+1]+arr[i]

for i in range(1, n - 1):  # 꿀통이 제일 오른쪽 있을때(벌하나가 제일 왼쪽)
    res = (sum_value - arr[0] - arr[i]) + (sum_value - sum_arr[i])
    max_value = max(max_value, res)

for i in range(n-2,-1,-1):  #꿀통이 제일 왼쪽,(벌하나가 제일오른)
    res = (sum_value - arr[n-1] - arr[i]) + (sum_value-sum_reverse_arr[i])
    max_value = max(max_value, res)

#꿀통이 중간, 별이 왼쪽 오른쪽
mid = n//2
res = sum_arr[mid]-arr[0] + sum_reverse_arr[mid]-arr[n-1]
max_value = max(max_value,res)

print(max_value)
