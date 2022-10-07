n , m , r , c = map(int,input().split())
dir = [input() for _ in range(m)]
#graph = [[0]*n for _ in range(n)]
r, c = r-1, c-1
up, right, front = 1, 3, 2,
#D, L, B = 7-U, 7-R, 7-F
res = []
num_dir = -1
dx,dy = [0,1,0,-1],[1,0,-1,0]
dir_mapper = {'R':0, 'D':1, 'L':2, 'U':3}
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dir_die(alphabet):#이동에 따른 주사위 초기화
    global up,right,front,num_dir,dir_mapper,r,c
    if alphabet == 'R':
        num_dir = dir_mapper[alphabet]
        if in_range(r+dx[num_dir],c+dy[num_dir]):
            right,front,up = up,front,7-right
            res.append(7-up)
    elif alphabet == 'D':
        num_dir = dir_mapper[alphabet]
        if in_range(r+dx[num_dir],c+dy[num_dir]):
            up,front,right = 7-front,up,right
            res.append(7-up)

    elif alphabet == 'L':
        num_dir = dir_mapper[alphabet]
        if in_range(r+dx[num_dir],c+dy[num_dir]):
            up,right,front = right,7-up,front
            res.append(7-up)

    elif alphabet == 'U':
        num_dir = dir_mapper[alphabet]
        if in_range(r+dx[num_dir],c+dy[num_dir]):
            front,up,right = 7-up,front,right
            res.append(7-up)
    r,c = r+dx[num_dir],c+dy[num_dir]
for i in dir:
    dir_die(i)
print(res)