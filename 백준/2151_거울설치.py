from collections import deque
n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dxs,dys = [0,0,1,-1],[1,-1,0,0] #동서남북
# 0:2,3 /  1:2,3  / 2: 0,1 / 3: 0,1
#동:남,북 / 서:남,북 / 남:동,서 / 북:동,서
dir_arr = [[2,3], [2,3], [0,1], [0,1]]
answer = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n
def bfs(x,y):
    global answer
    dir = -1
    visited[x][y] = 1
    que = deque()
    que.append((x,y))
    #dir 방향 정하고
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '#' and dir == -1:
                if i==0 : dir = 2
                elif i==n-1: dir=3
                elif j==0 : dir=0
                elif j==n-1 : dir = 1
    while que:
        dx,dy = que.popleft()
        # print("dx,dy",dx,dy)

        if graph[dx][dy] == '!':
            for i in dir_arr[dir]:
                dir = i
                nx,ny = dx+dxs[dir], dy+dys[dir]
                if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] != '*':
                    if graph[nx][ny] == '!':
                        visited[nx][ny] = 1
                        answer += 1
                        que.append((nx, ny))
                    elif graph[nx][ny] == '.':
                        visited[nx][ny] = 1
                        que.append((nx,ny))

                    if graph[nx][ny] == '#':
                        return

        elif graph[dx][dy] == '.' or graph[dx][dy]=='#':
            nx,ny = dx+dxs[dir], dy+dys[dir]
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] != '*':
                if graph[nx][ny] == '!':
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                    answer += 1
                elif graph[nx][ny] =='.':
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                if graph[nx][ny] == '#':

                    return

for i in range(n):
    for j in range(n):
        if graph[i][j] == '#' and( i==0 or j==0 or i==n-1 or j==n-1):
            # print("i,j",i,j)
            bfs(i,j)
            print(answer)
            exit(0)


