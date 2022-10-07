import sys

sys.setrecursionlimit(10 ** 6)

#면적이 15로도 풀수잇음
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def check(arr):  # 검사
    cnt = 0
    value = 0
    visited = [[0] * N for _ in range(N)]
    for t in arr:
        for i in range(5):
            nx, ny = t[0] + dx[i], t[1] + dy[i]
            cnt += 1
            value += garden[nx][ny]
            #if in_range(nx1, ny1) and not visited[nx1][ny1]:
            #    value += garden[nx1][ny1]
            #else:
            #    return False
    if cnt == 15:
        return value
    else:
        return False

N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 0, 1, 0]
dy = [0, -1, 1, 0, 0]
dp = [[0] * N for _ in range(N)]
answer = []

for i1 in range(1, N - 1):
    for j1 in range(1, N - 1):
        for i2 in range(i1+1, N - 1):
            for j2 in range(j1+1, N - 1):
                for i3 in range(i2+1, N - 1):
                    for j3 in range(j2+1, N - 1):
                        arr = [[i1, j1], [i2, j2], [i3, j3]]
                        x = check(arr)
                        if x:
                            answer.append(x)
                        else:
                            break

print(min(answer))
