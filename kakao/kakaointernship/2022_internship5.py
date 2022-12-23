rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
answer = [[]]
num_dir = 0
dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]  # 동 남 서 북
spare_rc = [[0] * (len(rc[0])) for _ in range(len(rc))]
for i in range(len(rc)):
    for j in range(len(rc[0])):
        spare_rc[i][j] = rc[i][j]
def in_range(x, y):
    return 0 <= x < len(rc) and 0 <= y < len(rc[0])
#def ShiftRow(rc):  # 행하나씩내리기
def Rotate(rc):  # 껍질만 시계방향으로 돌리기
    global num_dir
    dx, dy = 0, 0
    visited = [[0] * (len(rc[0])) for _ in range(len(rc))]
    visited[dx][dy] = 1
    spare = rc[1][0]
    tmp = 0
    while True:
        nx, ny = dx + dxs[num_dir], dy + dys[num_dir]
        print(nx,ny)
        if in_range(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = 1
            spare_rc[nx][ny] =rc[dx][dy]  # 이전값
            dx, dy = nx, ny
        elif  visited[nx][ny]:
            break
        else:
            num_dir = (num_dir + 1) % 4

Rotate(rc)
for i in spare_rc:
    print(i)

