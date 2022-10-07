n = int(input())
graph= [list(input()) for _ in range(n)]
dx = [0,0,1]
dy = [1,-1,0]
ox = [1,-1,0]
oy = [0,0,-1]
#행
res = 0
for x in range(n):  # 가로줄
    cnt = 1
    for y in range(n-1):
        if graph[x][y] == graph[x][y+1]:
            cnt+=1
        else:
            for i in range(3):
                nx = dx[i]+y
                ny = dy[i]+(x+1)
                if nx>=n or nx<0 or ny>=n or ny<0:
                    break
                if graph[x][y+1] == graph[nx][ny]:
                    a = graph[x][y+1]
                    graph[x][y+1] = graph[nx][ny]
                    graph[nx][ny] = a
                    cnt += 1
                    break
    res = max(cnt,res)

for x in range(n):  #좌표상
    cnt = 0
    for y in range(n-1):
        if graph[y][x] == graph[y+1][x]:
            cnt+=1
        else:
            for i in range(3):
                nx = ox[i]+y
                ny = oy[i]+(x+1)
                if nx>=n or nx<0 or ny>=n or ny<0:
                    break
                if graph[x+1][y] == graph[nx][ny]:
                    a = graph[x+1][y]
                    graph[x+1][y] = graph[nx][ny]
                    graph[nx][ny] = a
                    cnt += 1
                    break

print(res)