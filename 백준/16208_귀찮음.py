n = int(input())
arr = sorted(list(map(int,input().split())))
answer = 0
sum_value = sum(arr)

for i in range(n-1):
    sum_value -= arr[i]
    answer += arr[i] * sum_value
    #print(arr[i]*sum_value)
print(answer)