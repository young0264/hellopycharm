from bisect import bisect_left

t = int(input())
for _ in range(t):
    arr = [1000] * 1001
    cnt = 0
    n = int(input())
    input_arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = input_arr[i]
    for i in range(n):
        for j in range(n):
            if arr[j]>arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
                cnt += 1
    print(cnt)
