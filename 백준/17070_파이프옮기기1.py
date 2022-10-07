n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
dxs,dys = [0,1,1],[1,1,0] #오른쪽, 대각선, 아래
dic = {0:[0,1], 1:[0,1,2], 2:[1,2]}
# 0 -> 1 오른에서 대각
# 1 -> 0,2대각에서 오른 아래
# 2 -> 1아래에서 대각
answer = 0
visited = [[0]*n for _ in range(n)]
def dfs(x,y,visited,dir):
    global answer

    visited[x][y] = 1

    if x==n-1 and y==n-1:
        answer += 1
        print(x,y,dir)
        print("visited")
        for i in visited:
            print(*i)


    for new_dir in dic[dir]:
        nx,ny = x+dxs[new_dir], y+dys[new_dir],
        if in_range(nx,ny) and not visited[nx][ny] and not graph[nx][ny]:
            print("nx,ny",nx,ny)
            print()
            visited[nx][ny] = 1
            dfs(nx,ny,visited,new_dir)

dfs(0,1,visited,0)
print(answer)





















# #0 가로 -> 가로, 대각선
# #1 세로 -> 세로,대각선
# #2 대각선 -> 가로,세로,대각선
# cnt = 0
# dxs,dys = [0,1,1],[1,1,0] #오른쪽,대각선,아래 (0~1:가로, 1~2:세로, 0~2:대각선)
# def in_range(x,y):
#     return 0<=x<n and 0<=y<n
# visited = [[0]*n for _ in range(n)]
# def dfs(dx,dy,dir):
#     global cnt
#     visited[dx][dy] = 1
#     if dx == n - 1 and dy == n - 1:
#         cnt += 1
#         return
#
#     if dir ==0:
#         for i in range(2):
#             nx,ny = dx+dxs[i],dy+dys[i]
#             if in_range(nx,ny) and not visited[nx][ny] and not graph[nx][ny]:
#                 visited[nx][ny] = 1
#
#                 if i==1:
#                     dfs(nx,ny,1)
#                     visited[nx][ny] -= 1
#
#                 else :
#                     dfs(nx,ny,0)
#                     visited[nx][ny] -= 1
#
#
#     elif dir ==1:#세로
#         for i in range(1,3):
#             nx,ny = dx+dxs[i], dy+dys[i]
#             if in_range(nx,ny) and not visited[nx][ny] and not graph[nx][ny]:
#                 visited[nx][ny] = 1
#                 visited[nx][ny] -= 1
#
#                 if i==2:
#                     dfs(nx,ny,2)
#                     visited[nx][ny] -= 1
#
#                 else:
#                     dfs(nx,ny,1)
#                     visited[nx][ny] -= 1
#
#
#     else: #대각선
#         for i in range(3):
#             nx,ny = dx+dxs[i], dy+dys[i]
#             if in_range(nx,ny) and not visited[nx][ny] and not graph[nx][ny]:
#                 visited[nx][ny] = 1
#                 if i==0:
#                     dfs(nx,ny,0)
#                     visited[nx][ny] -= 1
#                 elif i ==1:
#                     dfs(nx,ny,1)
#                     visited[nx][ny] -= 1
#                 else:
#                     dfs(nx,ny,2)
#                     visited[nx][ny] -= 1
#
#
# visited[0][0] =
# dfs(0,1,0)
# print(cnt)






