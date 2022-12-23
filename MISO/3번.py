# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S):
    # write your code in Python 3.8.10
    answer = 0
    new_S = [[0] * 10 for _ in range(N)]
    S = S.split(' ')

    for s in S:
        if s:
            row = int(s[0]) - 1
            col = ord(s[-1]) - 65
            if col == 10 or col == 9:
                col -= 1
            new_S[row][col] = 1
# N^2
    for i in range(N):
        arr = new_S[i][:]

        # 모든 요소가 False일때
        if not any(arr[1:5]):
            answer += 1
            arr[1:5] = [1, 1, 1, 1]
        if not any(arr[3:7]):
            answer += 1
            arr[3:7] = [1, 1, 1, 1]
        if not any(arr[5:9]):
            answer += 1
            arr[5:9] = [1, 1, 1, 1]

    return answer

    pass
