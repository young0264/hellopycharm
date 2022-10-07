import sys
sys.setrecursionlimit(260000)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx,dy = [0,0,1,-1],[1,-1,0,0]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global max_value
    if visited[x][y] != 0 :##이게포인트
        return visited[x][y]

    for i in range(4):
        nx,ny = dx[i]+x,dy[i]+y
        if in_range(nx,ny) and graph[nx][ny] > graph[x][y] :
            visited[x][y] = max(dfs(nx,ny)+1 , visited[x][y])##이것과
    return visited[x][y]

max_value = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            max_value = max(dfs(i,j),max_value)

print(max_value+1)
#######################################
#BOTTOM UP 위상정렬
#from collections import deque
#indegree = [[0] * n for _ in range(n)] #--> 진입차수 --> 자기로 들어오는 애 == 자기 자식 수
#link = [[[] for _ in range(n)] for _ in range(n)]
#visited = [[1]*n for _ in range(n)]
#for x in range(n):
#    for y in range(n):
#        for d in range(4):
#            nx, ny = x + dx[d], y + dy[d]
#            if in_range(nx,ny) and graph[x][y] < graph[nx][ny]: # --> 제일 작은놈에서 시작해야 --> 부모를 갱신할 수 있음
#                link[x][y].append((nx,ny))
#                indegree[nx][ny] += 1
#queue = deque()
#ans = 1
#for i in range(n):
#    for j in range(n):
#        if not indegree[i][j]:
#            queue.append((i,j))
#while queue:
#    x,y = queue.popleft()
#    for nx,ny in link[x][y]:
#        visited[nx][ny] = max(visited[nx][ny],visited[x][y] + 1)
#        indegree[nx][ny] -= 1
#        if indegree[nx][ny] == 0: #--> 부모 노드의 indegree가 0이 됨 --> 자식들의 부모에 대한 갱신이 끝남
#            queue.append((nx,ny))
#            ans = max(ans,visited[nx][ny])
##print(*visited,sep="\n")
#print(ans)
