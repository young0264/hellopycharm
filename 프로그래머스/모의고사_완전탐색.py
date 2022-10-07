# 가장 많이 맞힌사람 Return
def solution(answers):
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    arr = [0] * 3
    # print("answers",answers)
    flag = 0

    for i in range(len(answers)):
        if answers[i] == a[i]:
            flag = 1
            arr[0] += 1
        if answers[i] == b[i]:
            flag = 1
            arr[1] += 1
        if answers[i] == c[i]:
            flag = 1
            arr[2] += 1

    max_value = -1
    if flag: max_value = max(arr)
    res = []
    for i in range(3):
        if not max_value == -1 and arr[i] == max_value:
            res.append(i + 1)
    return (res)
# [3, 3, 1, 1, 1, 1, 2, 3, 4, 5] -> [1, 3]
