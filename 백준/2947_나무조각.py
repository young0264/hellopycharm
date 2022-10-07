#arr = list(map(int, input().split()))
#ans_arr = sorted(arr)
#box = 0
#while True:
#    for i in range(4):
#        if arr[i] > arr[i + 1]:
#            box = arr[i]
#            arr[i] = arr[i + 1]
#            arr[i + 1] = box
#            print(*arr)
#            if arr == ans_arr:
#                exit(0)
#

arr = list(map(int, input().split()))
ans_arr = sorted(arr)
box = 0
while True:
    for i in range(4):
        if arr[i] > arr[i + 1]:
            box = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = box
            print(*arr)
            if arr == ans_arr:
                break
    if arr == ans_arr:
        break
