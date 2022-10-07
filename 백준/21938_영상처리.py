import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline()

r, c = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(r)]
graph = [[0]*c for _ in range(r)]
line = int(input())
visited = [[0]*c for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0
for i in range(r):
    for j in range(c):
        t= sum(x[i][j*3:j*3+3])
        graph[i][j] = t//3
#print(graph)



def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def dfs(x, y):
    global flag, line
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny]>=line:
            visited[nx][ny]=1
            #print(nx,ny)
            flag = 1
            dfs(nx, ny)
            #print(nx,ny)
    return True


for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j]>=line :
            visited[i][j] = 1
            if dfs(i, j):
                answer += 1
print(answer)
