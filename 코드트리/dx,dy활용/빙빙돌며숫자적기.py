#1. dx,dy 진행
#2. 벽에부딪혔는가
#3. 부딪히면 방향전환
#4. 값이 채워져있는지 확인도./ 이미 적혀있는칸은 막혀있는걸로 print

n, m = map(int, input().split())  # 행,열
arr = [[0] * m for _ in range(n)]
dir_num = 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0
arr[x][y] = 1

def in_range(x, y):
    return 0 <= x <n and 0 <= y <m

for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:  # !=0과 ==True의 차이 0 False가 아니면 트루아닌가
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()



