from collections import deque

def solution(grid):
    answer = 0

    row,col = len(grid), len(grid[0])
    arr = []
    for i in range(row):
        arr.append([i,0])
        arr.append([i,col-1])
    for i in range(1,col-1):
        arr.append([0,i])
        arr.append([row-1,i])
    graph =[list(i) for i in grid]
    visited = [[0]*col for _ in range(row)]
    dx,dy = [0,0,1,-1], [1,-1,0,0]
    def in_range(x,y):
        return 0<=x<row and 0<=y<col

    def bfs(si,sj):
        que = deque()
        que.append((si,sj))
        visited[si][sj] = 1

        while que:
            dxs,dys = que.popleft()
            for i in range(4):
                nx,ny = dx[i]+dxs, dy[i]+dys
                if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] != '#':
                    visited[nx][ny] = 1
                    que.append((nx,ny))

    for x,y in arr:
        if graph[x][y] != '#':
            bfs(x,y)
    for i in range(row):
        for j in range(col):
            if visited[i][j] == 0:
                answer += 1

    return answer

# solution([".#.", "#..", ".#."])
solution([".....####", "..#...###", ".#.##..##","..#..#...", "..#...#..","...###..."])