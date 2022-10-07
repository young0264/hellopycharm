NONE = -1
n = 4
graph = [list(map(int, input().split())) for _ in range(4)]
next_graph = [[0 for _ in range(n)] for _ in range(n)]
dir_mapper = {'D': 0, 'R': 1, 'U': 2, 'L': 3}
direction = input()


def rotate():
    for i in range(n):  # next graph 초기화
        for j in range(n):
            next_graph[i][j] = 0

    for i in range(n):
        for j in range(n):
            next_graph[i][j] = graph[n - 1 - j][i]

    for i in range(n):
        for j in range(n):
            graph[i][j] = next_graph[i][j]


def drop():
    for i in range(n):  # next graph 초기화
        for j in range(n):
            next_graph[i][j] = 0

    for j in range(n):
        next_row, num = n - 1, NONE
        for i in range(n - 1, -1, -1):
            if not graph[i][j]:  #####이걸뺴먹엇네
                continue

            if num == NONE:
                num = graph[i][j]

            elif num == graph[i][j]:
                next_graph[next_row][j] = num * 2
                num = NONE
                next_row -= 1
            else:
                next_graph[next_row][j] = num
                num = graph[i][j]
                next_row -= 1
        if num != NONE:
            next_graph[next_row][j] = num
            next_row -= 1  ###########

    for i in range(n):
        for j in range(n):
            graph[i][j] = next_graph[i][j]  # // next_graph -> graph로 복사


def tilt(move_dir):
    for _ in range(move_dir):
        rotate()
    drop()
    for _ in range(4 - move_dir):
        rotate()


tilt(dir_mapper[direction])
for i in graph:
    print(*i)


