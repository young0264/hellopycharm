from collections import deque
def bfs(x):
    global cnt
    q = deque()
    q.append(x)
    visited[x]=True
    while q:
        next = q.popleft()
        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return 1
    #return cnt

t = int(input())
for i in range(t):
    cnt = 0
    n=int(input())
    visited = [False] * (n + 1)
    graph = [[]*(n+1) for _ in range(n+1)]  #첫번째배열은 빈배열로
    arr = list(map(int,input().split()))
    sor_arr=sorted(arr)
    for j in range(n):
        graph[sor_arr[j]].append(arr[j])


    for i in range(1,n+1):
        #print(visited)
        if visited[i] == False: #1,3,5,7이 bfs(1)한방에 False가됬네
            cnt += bfs(i)   #1을 리턴
    print(cnt)

#    if sor_arr[j] in graph[arr[j]]:
   #        continue
   #    graph[arr[j]].append(sor_arr[j])
   #    if arr[j] in graph[sor_arr[j]]:
   #        continue









