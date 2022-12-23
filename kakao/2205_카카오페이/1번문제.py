

def solution(n,m,rectangle):
    dx,dy = [0,1],[1,0]
    graph = [[0]*n for _ in range(m)]
    visited =  [[0]*n for _ in range(m)]
    s_len = [0]*11
    answer = []
    rectangle = sorted(rectangle,key=lambda x:x[0])

    def in_range(x,y,size):
        for i in range(2):
            for j in range(1,size+1):
                nx,ny = x+dx[i]*j,y+dy[i]*j
                if visited[nx][ny]:
                    return False
        return True

    def check(x,y,size):
        visited[x][y] = 1
        for i in range(2):
            for j in range(1,size+1):
                nx,ny = x+dx[i]*j,y+dy[i]*j
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
    for a,b in rectangle:
        s_len[a]=b
    re=[]
    for t in range(len(rectangle)):
        x1,x2 = rectangle[t][0],rectangle[t][1]
        while x2 :
            for i in range(m):
                for j in range(n):
                    if in_range(i,j,x1):
                        check(i,j,x1)
                        x1 -= 1
                        re.append((i,j))
    return re


n,m = map(int,input().split())
rectangle = []
for i in range(3):
    a,b = map(int,input().split())
    rectangle.append([a,b])
solution(n,m,rectangle)



