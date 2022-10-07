n = int(input())
graph = [list(input()) for _ in range(n)]
friend = [[] for _ in range(n)]

#for i in range(n):
#    for j in range(n):
#        if graph[i][j] == 'Y':
#            friend[i].append(j+1)
#x = [[]] + friend
#print(x)
def dfs(x):
    stack = []
    visited = [-1]*n
    stack.append((x,0)) # idx, cnt
    visited[x] += 1
    total = 0
    while stack :
        now,cnt = stack.pop()
        for i in range(n):
            if graph[now][i]=='Y' and visited[i]==-1 and not cnt>=2:
                visited[i] = visited[now]+1
                stack.append((i,cnt+1))
                total +=1
    return total

answer = 0
for i in range(n):
    max_value = dfs(i)
    answer = max(max_value,answer)

print(answer)