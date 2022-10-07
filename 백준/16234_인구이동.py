#방문한 지점들의 위치를 배열에 담은후 그 위치의 평균값으로 초기화한다.
#해당그래프에 이동할껀덕지가 있으면// bfs실행하는 함수. while
#그래프는 sparegraph에 벼동
#
from collections import deque


def in_range(x,y):
    return 0<=x<N and 0<=y<N
def gap(x,y,nx,ny):
    if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
        return True
    return False

#0,0시작 조건에맞는것만 que에 담을거야
def bfs(x,y):
    global flag, box_cnt
    box_sum = graph[x][y]  # 깬 박스에 들어있는 값들
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    location.append(spare_graph[x][y])
    visitque = deque()
    visitque.append((x,y))

    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i],dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny]:
                if gap(dx,dy,nx,ny):
                    visited[nx][ny] = True
                    box_cnt += 1
                    box_sum += graph[nx][ny]
                    flag = True
                    que.append((nx,ny))
                    visitque.append((nx,ny))
                    location.append(spare_graph[nx][ny])
    while visitque:
        a,b = visitque.popleft()
        graph[a][b] = box_sum//box_cnt

N, L, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
spare_graph = [[0]*N for _ in range(N)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
answer = 0

while True:
    flag = 0
    location = []
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                box_cnt = 1  # 박스 카운팅
                res = bfs(i,j)
                count += 1

    if flag == 0:
        break
    else:
        answer += 1
print(answer)









