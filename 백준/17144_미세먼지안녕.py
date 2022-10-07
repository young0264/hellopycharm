r , c , t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
dir_num1 = 0
dir_num2 = 0
dxs = [1,0,-1,0] #동 , 남, 서, 북
dys = [0,1,0,-1]

x_locate = []
for i in range(r):
    if arr[i][0] == -1:
        x_locate.append(i)
x1,y1 = x_locate[0],0
x2,y2 = x_locate[1],0
print(x1,y1)
print(x2,y2)
def in_range(x,y):
    return 0<=x<r and 0<=y<c and arr[x][y] != -1

def up(x1,y1):  #위쪽 이동하는거
    global dir_num1
    nx = x1 + dxs[dir_num1]
    ny = y1 + dys[dir_num1]
    if not in_range(nx,ny) :
        dir_num1 = (dir_num1 + 3)%4

def down(x2,y2):    #아래쪽 이동하는거
    global dir_num2
    nx = x2 + dxs[dir_num2]
    ny = y2 + dys[dir_num2]
    if not in_range(nx,ny):
        dir_num2 = (dir_num2)%4

def mise(x,y):  #미세먼지가 퍼지는거
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if in_range(nx,ny):
            arr[nx][ny] += arr[x][y]//5
            arr[x][y] -= arr[x][y]





