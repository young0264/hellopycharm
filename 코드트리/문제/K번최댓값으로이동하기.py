from collections import deque

n, k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
r,c = map(int,input().split())
dxs, dys = [0,0,1,-1], [1,-1,0,0]
r,c = r-1, c-1
q = deque()
q.append((r,c))
count = 0

#범위
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_pos_by_maxVal(maxVal):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == maxVal:
                return (i,j)
    return (-1,-1)

#상하좌우, 자기보다 같거나 작은수, 너비탐색으로 이동
def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    max_val = 0
    # before_value = graph[x][y]
    # flag_x, flag_y = -1,-1
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
                que.append((nx,ny))
                max_val = max(max_val, graph[nx][ny])
                visited[nx][ny] = 1
    return max_val

while q:
    dx, dy = q.popleft()
    maxValue = bfs(dx,dy)
    nx,ny = find_pos_by_maxVal(maxValue)
    if nx==-1 and ny==-1:
        print(dx+1, dy+1)
        break
    else:
        count += 1
        q.append((nx,ny))
        if count == k:
            print(nx+1, ny+1)
            break

# #4방향에서 max값 찾기
# def find_max_value(x,y):
#     s = set()
#     for i in range(4):
#         nx,ny = x+dx[i], y+dy[i]
#         if in_range(nx,ny):
#             s.add(graph[nx][ny])
#     return(max(s))

# #maxValue 위치찾기 (가장작은 i,j)


# # r,c 에서 시작을 해서
# # r,c의 상하좌우의 값중에 최댓값 = value
# # graph[r][c]내에서 value에 해당하는 첫번째(i,j)를 que에 담음, break
# # 담으면 count += 1, now위치 초기화
# # if count == k : print(now)


# while que:
#     dx,dy = que.popleft()
#     max_value = find_max_value(dx,dy)
#     nx,ny = find_pos_by_maxVal(max_value)
#     if nx==-1 and ny==-1:
#         break
#     answer += 1

