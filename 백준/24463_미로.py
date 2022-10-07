#가장자리 끝점을 어떻게 찾냐
#가장자리 점 두개찾기
#이 문제에서 최단거리로 이동한다는 의미가 곧/ 아 성립한다는 의미가 아닐수가있어. 거쳐간 최소점을
#구할순있는데.. 음음from collections import deque
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
answer = [['']*c for _ in range(r)]#.을다 @. +는+로
visited = [[0]*c for _ in range(r)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
locate = [] #시작점과 끝점의 위치가 담겨있음
def in_range(x,y):
    return 0<=x<r and 0<=y<c
for i in range(r):
    if graph[0][i] == '.':
        locate.append([0,i])
    if graph[r-1][i] == '.':
        locate.append([r-1,i])
for i in range(c):
    if graph[i][0] == '.':
        locate.append([i,0])
    if graph[i][c-1] =='.':
        locate.append([i,c-1])
s1,s2,e1,e2 = locate[0][0],locate[0][1],locate[1][0],locate[1][1]


def dfs(s1,s2,e1,e2):
    visited[s1][s2] = True
    answer[s1][s2] = '.'
    for i in range(4):
        nx,ny = dx[i]+s1, dy[i]+s2
        if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] == '@':
            if nx==e1-1 and ny==e2-1:
                answer[nx][ny] = '.'
                return
            dfs(nx,ny,e1,e2)
            ##########################
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '+':
                answer[i][j] = '+'
            elif graph[i][j] == '.':
                answer[i][j] = '@'

dfs(s1,s2,e1,e2)
for i in answer:
    print(*i,sep='')