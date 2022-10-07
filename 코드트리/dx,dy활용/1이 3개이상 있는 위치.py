n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

def range_check(x,y):
    return 0 <= x < n and 0 <= y < n


def num_count(x,y):
    cnt = 0
    for dx,dy in zip(dxs,dys):
        nx , ny = dx+x, dy+y
        if range_check(nx,ny) and arr[nx][ny]==1:
            cnt +=1
    return cnt

answer = 0
for i in range(n):
    for j in range(n):
        if num_count(i,j) >= 3:
            answer += 1
print(answer)