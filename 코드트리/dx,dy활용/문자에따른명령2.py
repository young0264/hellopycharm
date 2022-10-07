#L이면 -1, R이면 +1하면 now_dir에 변화를주고
#F이면 그 방향으로 x,y에 변화를 주고

direction = input()
now_dir = 3
dx = [1,0,-1,0]
dy = [0,-1,0,1]
x,y = 0,0
#now_dir = (now_dir + 1)%4
for i in direction:
    if i =='L':
        now_dir = (now_dir-1)%4
    elif i =='R':
        now_dir = (now_dir+1)%4
    else:
        x = x+ dx[now_dir]
        y = y+ dy[now_dir]

print(x,y)