def solution(grid, k):
    answer = []
    r , c = len(grid),len(grid[0])
    visited = [[0]*c for _ in range(r)]
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    def in_range(x,y):
        return 0<=x<r and 0<=y<c #행열

    def dfs(x,y,cnt):
        visited[x][y] = 1
        if x == r-1 and y == c-1:
            return
        for i in range(4):
            dxs,dys = x+dx[i], y+dy[i]
            if in_range(dxs,dys) and  grid[dxs][dys] != "#" and not visited[dxs][dys]:
                visited[dxs][dys] = 1
                dfs(dxs,dys,cnt)




    #answer = -1
    #cnt 0
    return answer