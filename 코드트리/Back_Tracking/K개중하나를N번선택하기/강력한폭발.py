n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
bombed = [[0] * n for _ in range(n)]
bomb_type = [[0] * n for _ in range(n)] #이건 왜만든거지
def in_range(x,y):
    return 0<=x<n and 0<=y<n
bomb_now = []   #폭탄의 위치
bomb_number = 0    #폭탄의 총 갯수
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bomb_number += 1
            bomb_now.append((i,j))
#0:x, 1,2,3번 Index == 1,2,3번 폭탄
bomb_arr = [
    [[1,0],[2,0],[0,0],[-1,0],[-2,0]],
    [[1,0],[-1,0],[0,0],[0,1],[0,-1]],
    [[1,1],[1,-1],[0,0],[-1,1],[-1,-1]]
]
bomb_cnt = 0
bomb_max = 0
def get_max_bomb(n):    #n은 폭탄이 터진 자리수
    global bomb_cnt,bomb_max,bomb_number
    if n == bomb_number:
        bomb_max = max(bomb_cnt, bomb_max)
        return
    x,y = bomb_now[n]
    for i in range(3):
        for j in range(5):
            dx,dy = bomb_arr[i][j]
            nx, ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if not bombed[nx][ny]: # 방문안했으면
                bomb_cnt += 1
            bombed[nx][ny] += 1#방문처리#이전꺼를 -백트래킹 해주기위해선, +=1로

        get_max_bomb(n+1)#재귀
        for j in range(5):
            dx, dy = bomb_arr[i][j]
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            bombed[nx][ny] -= 1
            if not bombed[nx][ny]:  # 방문안했으면
                bomb_cnt -= 1

get_max_bomb(0)
print(bomb_max)

#인덱스 : bomb_now에 폭탄위치를 인덱스로 받아서 넣기
#numbers = []
#def permutations(cnt,box) : #numbers에 조합가능한 경우의수 삽입
#    if cnt == bomb_cnt:
#        numbers.append(box)
#        return
#    for i in range(1,4):
#        permutations(cnt+1,box+[i])
#

#def bomb(x,y,b_type):    # 해당위치...폭탄터트리기
#    for i in range(5):  #5번을 돌아서 해당폭탄 터트리기
#        dx,dy = bomb_arr[b_type][i]
#        nx,ny = dx+x,dy+y
#        if in_range(nx,ny):
#            bombed[nx][ny] = 1
#
#def calc():#후..ㅅ
#    for i in range(n):
#        for j in range(n):
#            bombed[i][j] = False
#    for i in range(n):
#        for j in range(n):
#            if bomb_type[i][j]:
#                bomb(i,j,bomb_type[i][j])
#    cnt = 0
#    for i in range(n):
#        for j in range(n):
#            if bombed[i][j]:
#                cnt += 1
