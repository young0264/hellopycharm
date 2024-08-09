def solution(s):
    answer = 0

    def is_same_3chars(arr, start):
        if arr[start] == arr[start + 1] == arr[start + 2]:
            return True
        return False

    arr = []
    arr_s = list(s)

    for i in range(0, len(s) - 2):
        if is_same_3chars(arr_s, i):
            arr.append(arr_s[i:i + 3])

    if(len(arr) == 0): # 멋쟁이 수가 없을 때
        return -1

    for i in range(len(arr)):
        answer = max(answer, int(''.join(arr[i])))

    if(answer == 0): # 멋쟁이 수가 000 일 때
        return 0
    return answer