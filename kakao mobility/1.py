def solution(flowers):
    answer = 0
    arr = [0] * 166
    for a, b in flowers:
        for i in range(a, b):
            arr[i] = 1

    for i in arr:
        if i: answer += 1

    return answer
