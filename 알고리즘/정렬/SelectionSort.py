n = int(input())
arr = list(map(int,input().split()))

for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    tmp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = tmp
print(*arr)
