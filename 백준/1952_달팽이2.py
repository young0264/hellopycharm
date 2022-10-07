def in_range(x,y):
    return 0<=x<r and 0<=y<c and not graph[x][y]
r , c = map(int,input().split())
graph = [[0]*c for _ in range(r)]
cnt = 0
dx = [0,1,0,-1]#행 동남서북,
dy = [1,0,-1,0]#열
num_dir=0
graph[0][0] = r*c
x,y = 0,0
for i in range(r*c-1,0,-1): #-1부터시작
    nx = x + dx[num_dir]
    ny = y + dy[num_dir]
    if in_range(nx,ny):
        graph[nx][ny] = i
        x , y = nx,ny
    else:
        num_dir = (num_dir+1)%4
        nx = x + dx[num_dir]
        ny = y + dy[num_dir]
        graph[nx][ny] = i
        x,y=nx,ny
        cnt += 1
    if graph[x][y] == 1:
        print(cnt)
        #print(x+1,y+1)      #1,1부터 행렬은 시작하기때문에 +1씩해주기
        exit(0)