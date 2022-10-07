t = int(input())
arr = []
answer = 0
for i in range(t):
    arr.append(int(input()))

arr = list(reversed(arr))

for i in range(1,t):
    if arr[i-1] <= arr[i] :
        answer += arr[i]-arr[i-1]+1
        arr[i] = arr[i-1]-1
print(answer)