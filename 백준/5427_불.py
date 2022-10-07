from collections import deque
import sys

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def bfs():
    global max_value
    while que:
        dx, dy = que.popleft()
        for i in range(4):
            nx, ny = dx + dxs[i], dy + dys[i]

            if not in_range(nx, ny) and visited[dx][dy] > 0:
                return visited[dx][dy]

            if in_range(nx, ny)  and graph[nx][ny] == '.'  :
                if not visited[nx][ny] and visited[dx][dy] > 0:
                    visited[nx][ny] = visited[dx][dy] + 1
                    que.append((nx, ny))
                elif visited[dx][dy] < 0 and visited[nx][ny]>=0:
                    visited[nx][ny] = visited[dx][dy] - 1
                    que.append((nx,ny))

t = int(input())

for _ in range(t):
    c,r = map(int, input().split())
    graph = [list(input()) for _ in range(r)]
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    que = deque()
    visited = [[0] * c for _ in range(r)]

    # F,J위치찾기
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "@":
                que.append((i,j))
                visited[i][j] = 1

    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                que.append((i,j))
                visited[i][j] = -1
    x = bfs()
#    for i in visited:
#        print(*i)
    if x:
        print(x)
    else:
        print("IMPOSSIBLE")

