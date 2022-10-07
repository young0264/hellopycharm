def solution(rows, columns, queries):
    def in_range(x, y):
        return x1 <= x <= x2 and y1 <= y <= y2

    graph = [[0] * columns for _ in range(rows)]
    answer = []
    dir = -1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 행열, 동남서북
    cnt = 0
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(rows):
        for j in range(columns):
            cnt += 1
            graph[i][j] = cnt

    for a, b, c, d in queries:
        x1, y1, x2, y2 = a - 1, b - 1, c - 1, d - 1
        tmp = graph[x1][y1]
        px, py = x1, y1
        for i in range(x2 - x1 + y2 - y1):
            dir = 0
            nx, ny = px + dx[dir], py + dy[dir]
            if in_range(nx, ny):
                graph[nx][ny] = graph[px][py]
                px, py = nx, ny
            else:
                dir += 1
                nx, ny = px + dx[dir], py + dy[dir]
                graph[nx][ny] = graph[px][py]
                px, py = nx, ny
            if nx == x1 and ny == y1:
                graph[nx][ny] = tmp
                break
        print()
        print(nx, ny)

    return answer