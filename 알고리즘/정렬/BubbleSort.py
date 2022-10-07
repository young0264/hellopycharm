n = int(input())
arr = list(map(int,input().split()))
while True:
    flag = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            flag = 1
    if flag==-1:
        break
print(*arr)