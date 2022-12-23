# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, T):
    # write your code in Python 3.8.10
    length = len(D)
    dist = [0] * length
    dist[0] = D[0] * 2
    answer = 0

    for i in range(1, length):
        dist[i] = D[i] * 2 + dist[i - 1]

    dp = [[0] * length for _ in range(3)]

    max_p, max_g, max_m = 0, 0, 0
    for j in range(length):
        p, g, m = 0, 0, 0  # 각 열마다 p,g,m 갯수세기
        for k in T[j]:
            if k == 'P':
                p += 1
            elif k == 'G':
                g += 1
            elif k == 'M':
                m += 1
        # 알파벳이 나올때만 초기화
        if p:
            dp[0][j] = max_p + p
            max_p += p
        if g:
            dp[1][j] = max_g + g
            max_g += g
        if m:
            dp[2][j] = max_m + m
            max_m += m

    # 마지막 방문한 곳의 거리 max값 초기화
    for j in range(length):
        p, g, m = dp[0][j], dp[1][j], dp[2][j]
        if p:
            answer = max(answer, p + dist[j])
        if g:
            answer = max(answer, g + dist[j])
        if m:
            answer = max(answer, m + dist[j])
    return answer

    pass
