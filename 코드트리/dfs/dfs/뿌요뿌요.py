n = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, now):
    global cnt, max_value
    visited[x][y] = True
    cnt += 1
    now = graph[x][y]
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == now:
            dfs(nx, ny, now)
    if cnt >= 4:
        return True
    else:
        return False

max_value = -1
area_cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt = 0
            if dfs(i, j, 0):
                max_value = max(max_value, cnt)
                area_cnt += 1
            else:
                max_value = max(max_value, cnt)

print(area_cnt, max_value)