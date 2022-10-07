#양쪽값을 합하면 3
#키값을 마음대로 하고 싶을때 dictionary 사용
n, t = map(int, input().split())
r, c, d = map(str, input().split())
r = int(r)
c = int(c)
graph = [[0] * n for _ in range(n)]
# 대칭을 위할때는
dxs = [0, 1, -1, 0]  # 거꾸로 뒤집어주기 위해 변경함
dys = [1, 0, 0, -1]
mapper = {
    'R': 0,
    'L': 3,
    'U': 2,
    'D': 1
}
x,y = r-1,c-1
now_dir = mapper[d]
cnt = 0
def range_check(x, y):
    return 0 <= x < n and 0 <= y < n
        ##

for _ in range(t):
    nx = x + dxs[now_dir]
    ny = y + dys[now_dir]
    if range_check(nx,ny):
        x,y=nx,ny
    else:
        now_dir = (3-now_dir)%4 #or 3 - now_dir
print(x+1,y+1)



