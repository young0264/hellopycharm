n, t = map(int,input().split())
directions = input()
graph = []
dir = 3
# 동남서북 0,1,2,3
# R: (dir+1)%4, L: (dir+3)%4
#
def in_range(x,y):
    return 0<=x<n and 0<=y<n

for _ in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)
nowX, nowY = n//2, n//2
answer = graph[nowX][nowY]

for d in directions:
    if d == 'R':
        dir = (dir+1)%4
    elif d == 'L':
        dir = (dir+3)%4
    elif d == 'F':
        nx, ny = -1, -1
        if dir == 0:
            nx, ny = nowX, nowY+1
        elif dir==1:
            nx, ny = nowX+1, nowY
        elif dir==2:
            nx, ny = nowX, nowY-1
        elif dir==3:
            nx, ny = nowX-1, nowY

        if in_range(nx,ny):
            nowX , nowY = nx,ny
            answer += graph[nx][ny]

print(answer)
# RFFLFLF

