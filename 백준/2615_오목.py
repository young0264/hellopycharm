import sys
input = sys.stdin.readline
omok = [list(map(int,input().split()))for _ in range(19)]
dx = [0,1,1,-1] #[1,1,1,0]
dy = [1,1,0,1] #[0,1,-1,-1]

for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            for k in range(4):
                cnt = 1
                nx = dx[k]+ i
                ny = dy[k]+ j   #if 가아니라 while  #이 while문 아이디어.익히기
                while 0 <= nx <19 and 0 <= ny <19 and omok[nx][ny] == omok[i][j] :
                    cnt += 1    #육목제거 두가지 condition
                    if cnt == 5:
                        if 0<=i-dx[k]<19 and 0<=j-dy[k]<19 and omok[i-dx[k]][j-dy[k]]==omok[i][j]:
                            break
                        if 0<=nx+dx[k]<19 and 0<=ny+dy[k]<19 and omok[nx+dx[k]][ny+dy[k]]==omok[i][j]:
                            break
                        print(omok[i][j])
                        print(i+1,j+1)
                        exit(0)
                    nx += dx[k]
                    ny += dy[k]
print(0)
