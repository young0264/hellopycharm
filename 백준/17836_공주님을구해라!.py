from collections import deque
m, n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def in_range(x, y):
    return 0 <= x < m and 0 <= y < n
weapon1,weapon2 = -1,-1
# 장애물 신경쓰기
visited1 = [[-1] * n for _ in range(m)]
def bfs1(s1, s2):
    flag = 0
    global weapon1,weapon2,princess
    visited1[s1][s2] = 0
    que = deque()
    que.append((s1,s2))
    while que:
        dxs,dys = que.popleft()
        for i in range(4):
            nx, ny = dxs + dx[i] , dys+dy[i],
            if in_range(nx,ny) and graph[nx][ny]!=1 and visited1[nx][ny]==-1 :
                if graph[nx][ny]==2 and not flag:
                    weapon1,weapon2 = nx,ny
                    flag = 1
                que.append((nx,ny))
                visited1[nx][ny] = visited1[dxs][dys]+1

# 장애물 신경 안 쓰 기
visited2 = [[-1] * n for _ in range(m)]
def bfs2(s1, s2):   #오른쪾 아래만 가도되긴 하는데
    visited2[s1][s2] = 0
    que = deque()
    que.append((s1,s2))
    while que:
        dxs,dys = que.popleft()
        for i in range(4):
            nx, ny = dxs + dx[i] , dys+dy[i]
            if in_range(nx,ny) and visited2[nx][ny]==-1:
                visited2[nx][ny] = visited2[dxs][dys]+1
                que.append((nx,ny))

bfs1(0,0) #모든 그래프를 탐색 -> 무기위치,(m,n)의 위치도 파악
if weapon1 != -1 and weapon2 != -1:#얻은 무기가 있어야 탐색
    bfs2(weapon1,weapon2)
noknife , yesknife = -1,-1
#1.무기없이도달 2.무기하고도달
if visited1[m-1][n-1] != -1:
    noknife = visited1[m-1][n-1]        #칼없이 도달햇을때 값 초기화
if visited2[m-1][n-1] != -1:        #저 위치가 초기화됬다는건 무기가 있다는말
    yesknife = visited2[m-1][n-1]       #무기까지 도달한시간을 계산해줘야대

answer = 0

if noknife == -1 and yesknife == -1:
    print("Fail")
    exit(0)
elif noknife == -1:
    answer = visited1[weapon1][weapon2] + visited2[m-1][n-1]
elif yesknife == -1:
    answer = visited1[m-1][n-1]
else:
    answer = min(visited1[weapon1][weapon2] + visited2[m-1][n-1] ,visited1[m-1][n-1])

if answer > t:
    print("Fail")
    exit(0)
print(answer)
