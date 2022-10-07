n,m=map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
#x, y = r,c
dir_num  = d
dxs = [0,1,0,-1] #북,동,남,서
dys = [1,0,-1,0]

#dxs[dir_num]
#dys[dir_num]
def in_range(x,y):
    return 1<= x <n-1 and 1<= y <m-1 #범위벗어나면 False

def clean(x,y):
    global cnt, dir_num
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]
    if not in_range(nx,ny) and graph[nx][ny]==1:
        dir_num = (dir_num+3)%4 #반시계로 방향바꾸고

    graph[nx][ny] = 0
    x = nx
    y = y+dys[dir_num]
        cnt += 1