import copy
r,c = map(int,input().split())
map = [list(map(str,input())) for _ in range(r)]
check_map = copy.deepcopy(map)
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c
cnt = 0
def check(x,y):#X일때 check함수 실행하도록
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx,ny):
            cnt += 1
        else:
            if map[nx][ny] == '.':
                cnt +=1
    if cnt >= 3:
        check_map[x][y] = '.'
    cnt=0

for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            check(i,j)

row = []
col = []
for i in range(r):
    for j in range(c):
        if check_map[i][j] == 'X':
            row.append(i)
            col.append(j)
row.sort()
col.sort()
for i in range(row[0],row[-1]+1):
    for j in range(col[0],col[-1]+1):
        print(check_map[i][j],end='')
    print()