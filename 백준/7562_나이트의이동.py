from collections import deque
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def bfs(x,y):
    global n,goal_x,goal_y
    cnt = 0
    q = deque()
    visited = [[0]*n for _ in range(n)]
    q.append((x,y))
    visited[x][y] = True
    while q:
        cnt += 1
        for t in range(len(q)):
            a, b = q.popleft()
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if in_range(nx,ny) and visited[nx][ny]==0:
                    if nx == goal_x and ny == goal_y:
                        return cnt
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    return 0

dx,dy = [-1,-1,-2,-2,1,1,2,2],[-2,2,-1,1,-2,2,-1,1] #행,열
t = int(input())
for i in range(t):
    n = int(input())
    now_x, now_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())
    print(bfs(now_x,now_y))
