from collections import deque
F, S, G, U, D = map(int, input().split())

# S -> G 층에 가야하고 못가는 경우에는 해당 문자열 출력
def in_range(x):
    return 0 < x <= F

def bfs(x):
    visited = [-1] * (F + 1)
    que = deque()
    que.append(x)
    visited[x] += 1
    while que:
        dx = que.popleft()
        if dx == G:
            return visited[dx]
        arr = [dx + U, dx - D]
        for nx in arr:
            if in_range(nx) and visited[nx] == -1:
                visited[nx] = visited[dx] + 1
                que.append(nx)
    return -1

answer = bfs(S)
if answer != -1:
    print(answer)
else:
    print("use the stairs")
