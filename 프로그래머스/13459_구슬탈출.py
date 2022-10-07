from collections import deque


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


r, c = map(int, input().split())
base_graph = [list(input()) for _ in range(r)]
graph = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        graph[i][j] = base_graph[i][j]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[0] * c for _ in range(r)]  # Red


def bfs(x, y, x2, y2):
    global que
    visited[x][y] = 1
    que = deque()
    que.append((x, y))
    que.append((x2, y2))
    while que:
        dx, dy = que.popleft()
        print("dx,dy",dx,dy)
        if base_graph[dx][dy] == 'O' and graph[dx][dy] == 'R' and visited[dx][dy] < 11:
            return 1

        for i in range(4):
            nx, ny = dx + dxs[i], dy + dys[i],
            while True:
                if in_range(nx,ny) and

    return 0


r1, r2, b1, b2 = 0, 0, 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'R':
            r1, r2 = i, j
        elif graph[i][j] == 'B':
            b1, b2 = i, j
answer = bfs(r1, r2, b1, b2)  # que에 R와 B의 위치를 집어넣어
print(answer)