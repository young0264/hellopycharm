n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
next_graph = [[0] * n for _ in range(n)]  # 새로운배열
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
r, c = map(int, input().split())


# x,y둘중하나범위에 들고#그차의 합이(x,y중하나겟지)
def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(center_x, center_y):
    bomb_range = graph[center_x][center_y]

    # 폭탄이 터질 위치에 0으로 채워준다. 저 조건에 만족하면 그 위치에 0
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                graph[i][j] = 0

    for j in range(n):  # 외우기! 오
        next_row = n - 1  # 최하단행# 저장해놓고 한칸씩 옮겨가는걸로
        for i in range(n - 1, -1, -1):  # 최하단행
            if graph[i][j]:
                next_graph[next_row][j] = graph[i][j]
                next_row -= 1


bomb(r - 1, c - 1)
for i in next_graph:
    print(*i)

