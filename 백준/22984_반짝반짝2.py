n = int(input())
arr = list(map(float,input().split()))
answer = 0
answer += sum(arr)
for i in range(n-1):
    answer += arr[i]*(1-arr[i+1]) + (1-arr[i])*arr[i+1]
print(answer)
