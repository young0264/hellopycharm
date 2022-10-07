t = int(input())
for i in range(t):
    n=int(input())
    cnt = 0
    max_idx = -1
    arr = [0]*n

#arr초기화
    for i in range(n):
        num = int(input())
        arr[i] = num

    sum_value = sum(arr)
    max_value = max(arr)

    for i in range(n):
        if max_idx == - 1 and arr[i] == max_value:
            max_idx = i
        elif arr[i] == max_value:
            cnt += 1

    if max_value > sum_value-max_value:
        print("majority winner",max_idx+1)
        continue
    elif cnt == 0:
        print("minority winner", max_idx+1)
    else:
        print("no winner")
    #
    # if p == max(arr):
    #     print('no winner', )
    # elif p > sum(arr):
    #     print('majority winner', )
    # elif p <= sum(arr):
    #     print('minority winner', )