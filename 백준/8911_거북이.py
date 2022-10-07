#x,y좌표를 최대최소를 초기화하는식, 배열을 만들어서 표시할려니까 0,0에서의 마이너스구현이 복잡해짐
import sys
input = sys.stdin.readline
dx,dy=[1,0,-1,0],[0,-1,0,1] #동남서북#좌표기준으로
n = int(input())
def move(l):
    global num_dir, x , y,max_x,max_y,min_x,min_y
    if l == 'F':
        x,y = x+dx[num_dir], y+dy[num_dir]
    elif l == 'L':
        num_dir = (num_dir+3)%4
    elif l == 'R':
        num_dir = (num_dir+1)%4
    elif l == 'B':
        x,y = x-dx[num_dir] , y-dy[num_dir]
    max_x,max_y = max(max_x,x),max(max_y,y)
    min_x,min_y = min(min_x,x),min(min_y,y)

for _ in range(n):
    graph = [[0]*500 for _ in range(500)]
    num_dir = 3
    x, y = 0, 0
    order = list(input())
    max_x,max_y,min_x,min_y = 0,0,0,0
    for i in order:
        move(i)
    print((max_x-min_x)*(max_y-min_y))

