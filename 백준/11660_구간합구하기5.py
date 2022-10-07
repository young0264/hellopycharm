import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

#왼쪽,위에 공백의 행렬을 추가하든
#-1이 나오게해서 오른쪽, 아래에 0을 추가하든. 대책을 강구해야함.
#행에서 -1이면 아래로가고, 열에서-1이면 오른쪽끝이기 때문
visited = [[0]*(n+1) for _ in range(n+1)]
visited[0][0] = graph[0][0]

for i in range(n-1):
    visited[i+1][0] = graph[i+1][0] + visited[i][0]
    visited[0][i+1] = graph[0][i+1] + visited[0][i]

for i in range(n-1):
    for j in range(n-1):
        visited[i+1][j+1] = visited[i][j+1] + visited[i+1][j] + graph[i+1][j+1] - visited[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    minus = visited[x2-1][y1-2]+visited[x1-2][y2-1]-visited[x1-2][y1-2]
    ans = visited[x2-1][y2-1] - minus
    #print("x1,y1,x2,y2",x1,y1,x2,y2)

    print(ans)

#print("visited")
#for i in visited:
#    print(*i)
#print("v value",visited[3][-1])

