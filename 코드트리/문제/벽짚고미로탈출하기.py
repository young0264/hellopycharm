# 진행방향 앞에 벽이 있으면 반시계방향으로
## 진행방향 앞에 벽이 없고, 현재위치에서 우측에 벽이 있고, 앞&우측에 벽이 없을 때 -> 앞우측으로 이동 count += 2
##(진행방향 앞에 벽이 없고, 현재위치에서 우측에 벽이 있고, 앞&우측에 벽이 있으면 직진)
# 앞이 .이면 진행

# 1. 현재위치에서 오른쪽에 벽이 없으면 오른쪽으로 진행 + dir 수정
# 2. 진행방향 앞에 벽이 있으면 반시계 방향으로 dir 수정
from collections import deque

n = int(input())
x, y = map(int, input().split())
x, y = x - 1, y - 1
graph = [list(input()) for _ in range(n)]
visited = [[[0]*n for _ in range(n)] for _ in range(4)]

que = deque()
que.append((x, y))
dir = 0  # 0:동, 1:남, 2:서, 3:북
dir_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 일단 갈 수 있으면 가 answer += 1
# 항상 오른쪽을 체크해
    # 오른쪽에 뭐가 없으면 방향을 시계방향으로 90도 틀어
# 앞이 벽이어서 못가면 반시계방향으로 90도 틀어
#
#갇혀있는 체크?
#뺑글뻉글 도는 체크? -> 시작 x, y, 0 이면 뺑글도는거

while que:
    dx, dy = que.popleft()
    nx, ny = dx + dir_arr[dir][0] , dy + dir_arr[dir][1]
    # if nx == x and ny == y and dir == 0:
        # answer = 0
        # break
    print(dx,dy,dir)
    if in_range(nx,ny):
        r_dir = (dir+1)%4
        r_nx, r_ny = nx + dir_arr[r_dir][0], ny+dir_arr[r_dir][1]
        if graph[nx][ny] == '#':
            dir = (dir+3)%4
            que.append((dx,dy))
            if dir == 0 and dx == x and dy == y:
                answer = 0
                break
        elif graph[nx][ny] == '.':
            if graph[r_nx][r_ny] == '.' : #오른쪽에 아무것도 없으면
                dir = (dir+1)%4
                que.append((nx,ny))
                answer += 1
            elif graph[r_nx][r_ny] == '#' : #오른쪽에 벽이 있는 경우라면
                que.append((nx,ny))
                answer += 1
    else:
        answer += 1
        break



if not answer:
    print(-1)
else:
    print(answer)


#1. 바라보고 있는 방향으로 이동이 불가능한 경우(벽) -> 반시계 방향으로 90도 방향바꿈
#2. 이동이 가능한경우 -> 격자 밖이면 탈출

# dir방향으로 이동했을 때, 우측에 벽이 있으면 정상 이동
# dir방향으로 이동했을 때, 우측에 벽이 없으면 -> 시계방향으로 90도 돌려서 한칸 전진

