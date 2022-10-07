from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<n
n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dic = dict()  # 뱀의 변환정보
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 동남서북
dx, dy = 0, 0
dir = 0  # 동

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

que = deque()  # 큐에 뱀의 위치와 길이 담기

l = int(input())
for _ in range(l):
    a, b = map(str, input().split())
    dic[int(a)] = b
time_cnt = 0
que.append((0,0))
while True:
    time_cnt += 1
    nx,ny = dx + dxs[dir], dy + dys[dir]
    dx,dy = nx,ny

    if not in_range(nx,ny) or visited[nx][ny] == 1:
        break
    #방문한 지점에 사과가 있으면 길이 늘리기. else 길이 늘리고 줄이기
    #visited 체크해줘야할듯. 아닐수도##
    if graph[nx][ny] :
        que.append((nx,ny))
        graph[nx][ny]=ㅋ0
        visited[nx][ny] = 1
    else:
        a,b=que.popleft()
        visited[a][b] = 0
        que.append((nx,ny))
        visited[nx][ny] = 1

    #진행한곳이 X초라면 방향전환
    if time_cnt in dic and dic[time_cnt] != 0:
        if dic[time_cnt] == 'D':
            dir = (dir+1)%4
        elif dic[time_cnt] == 'L':
            dir = (dir+3)%4

print(time_cnt)
