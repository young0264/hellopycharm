res = []
n, r, c = map(int,input().split())
r = r-1
c = c-1
graph = [list(map(int,input().split())) for _ in range(n)]
res.append(graph[r][c])
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def can_go(x,y,num):#방문할좌표,현재값
    return in_range(x,y) and graph[x][y] > num
def simulate():
    global r,c
    dxs,dys = [1,-1,0,0],[0,0,1,-1]
    for dx,dy in zip(dxs,dys):
        nx,ny = dx+r , dy+c
        if can_go(nx,ny,graph[r][c]):
            r,c = nx,ny
            return True
    return False

while True:
    if not simulate():
        print(1)
        break
    #simulate가 True이면
    res.append(graph[r][c])

print(*res)